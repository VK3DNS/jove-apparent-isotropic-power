from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QSlider, QApplication, QComboBox, QLabel, QLineEdit, QPushButton, QTextEdit, QDateEdit, QTimeEdit, QCheckBox
import sys
from PySide6.QtCore import Qt, QTimer
import asyncio
import get_lat_long_dist
import datetime
import savefile

print(datetime.datetime.now())


class MainWindow(QMainWindow):
    def __init__(self, communicate, values, rx, tx, calc):
        self.firstloop = True
        super().__init__()

        defaults = savefile.load()

        self.jupiter = get_lat_long_dist.ObjectData()

        self.communicate = communicate
        self.values = values
        self.rx = rx
        self.tx = tx
        self.calc = calc

        layout = QVBoxLayout()

        self.setWindowTitle("Widgets App")

        self.lat_label = QLabel("Latitude:")
        layout.addWidget(self.lat_label)
        self.lat_input = QLineEdit()
        self.lat_input.setText(str(defaults["lat"]))
        layout.addWidget(self.lat_input)

        self.lon_label = QLabel("Longitude:")
        layout.addWidget(self.lon_label)
        self.lon_input = QLineEdit()
        self.lon_input.setText(str(defaults["lon"]))
        layout.addWidget(self.lon_input)

        self.alt_label = QLabel("Altitude (m):")
        layout.addWidget(self.alt_label)
        self.alt_input = QLineEdit()
        self.alt_input.setText(str(defaults["elev"]))
        layout.addWidget(self.alt_input)

        self.custom_time_label = QLabel("Custom Date & Time:")
        layout.addWidget(self.custom_time_label)
        self.date_input = QDateEdit()
        self.date_input.setDate(datetime.datetime.strptime(defaults["date"], "%Y-%m-%d").date())
        layout.addWidget(self.date_input)
        self.time_input = QTimeEdit()
        self.time_input.setDisplayFormat("HH:mm:ss")
        self.time_input.setTime(datetime.datetime.strptime(defaults["time"] if len(defaults["time"]) == 8 else defaults["time"][:-7], "%H:%M:%S").time())
        layout.addWidget(self.time_input)
        self.timezone_dropdown_label = QLabel("Timezone:")
        layout.addWidget(self.timezone_dropdown_label)
        self.timezone_dropdown = QComboBox()
        self.timezone_dropdown.addItems(f'GMT{"+" if i >= 0 else "-"}{-1*i if i < 0 else i}' for i in range(-11, 13))
        self.timezone_dropdown.setCurrentIndex(defaults["timezone"])
        layout.addWidget(self.timezone_dropdown)

        self.use_custom_time_label = QLabel("Use Custom Date & Time:")
        layout.addWidget(self.use_custom_time_label)
        self.use_custom_time = QCheckBox()
        self.use_custom_time.setChecked(defaults["use_custom_time"])
        self.use_custom_time_was_checked = defaults["use_custom_time"]
        self.use_custom_time.stateChanged.connect(self.update)
        layout.addWidget(self.use_custom_time)

        self.antenna_temp_label = QLabel("Antenna Temp (K):")
        layout.addWidget(self.antenna_temp_label)
        self.antenna_temp = QLineEdit()
        self.antenna_temp.setText(str(defaults["antenna_temp"]))
        layout.addWidget(self.antenna_temp)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)

        self.auto_update_label = QLabel("Auto Update:")
        layout.addWidget(self.auto_update_label)
        self.auto_update = QCheckBox()
        self.auto_update.setChecked(defaults["auto_update"])
        self.auto_update_was_checked = defaults["auto_update"]
        self.date_before_auto_update = self.date_input.date().toPython()
        self.time_before_auto_update = self.time_input.time().toPython()
        layout.addWidget(self.auto_update)

        self.update_button = QPushButton("Update")
        layout.addWidget(self.update_button)
        self.update_button.clicked.connect(self.update_button_func)

        '''
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(100, 600)
        self.slider.setSingleStep(3)
        self.slider.valueChanged.connect(self.value_changed)
        self.slider.sliderMoved.connect(self.slider_position)
        self.slider.sliderPressed.connect(self.slider_pressed)
        self.slider.sliderReleased.connect(self.slider_released)
        layout.addWidget(self.slider)
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        '''

        self.update()

    def update_button_func(self):
        self.update(new_datetime=True)

    def update(self, new_datetime=False):
        self.jupiter.lat = self.get_latitude()
        self.jupiter.lon = self.get_longitude()
        self.jupiter.elev = self.alt_input.text()

        custom_timezone = self.timezone_dropdown.currentIndex() - 11

        date = self.date_input.date().toPython() if self.use_custom_time.isChecked() else (datetime.date.today() if self.auto_update.isChecked() else self.date_before_auto_update)
        time = self.time_input.time().toPython() if self.use_custom_time.isChecked() else (datetime.datetime.now().time() if self.auto_update.isChecked() else self.time_before_auto_update)

        if new_datetime and not self.use_custom_time.isChecked():
            date = datetime.date.today()
            time = datetime.datetime.now().time()
            self.date_before_auto_update = date
            self.time_before_auto_update = time


        real_datetime = datetime.datetime.combine(date, time, datetime.timezone(datetime.timedelta(hours=custom_timezone)))
        custom_datetime = datetime.datetime.combine(date, time, datetime.timezone(datetime.timedelta(hours=custom_timezone)))
        self.jupiter.update_values(real_datetime if not self.use_custom_time.isChecked() else custom_datetime)

        num = float(str(self.jupiter.distance)[:-3])*10**7

        self.communicate.set_AuD.emit(num)
        self.communicate.get_values.emit()

        self.calc.K = float(self.antenna_temp.text() if self.antenna_temp.text().isnumeric() else 9.1 * 10 ** 4)

        self.calc.calculateisotropicpower()

        isopower = self.values["IsotropicPower"]

        self.output_box.setPlainText(f"Date: {date}\nTime: {time}\nTime zone: GMT{'+' if custom_timezone >=0 else ''}{custom_timezone}\n\nDistance: {self.jupiter.distance}\nAlt: {self.jupiter.alt}\nAz: {self.jupiter.az}\n\nApparent Power: {isopower}\n\nData valid: {int(self.jupiter.sunalt.split('d')[0]) <= -18 and int(self.jupiter.alt.split('d')[0]) >= 20}")

    def get_longitude(self):
        return self.lon_input.text()

    def get_latitude(self):
        return self.lat_input.text()

    def timerloop(self):
        if self.use_custom_time.isChecked() and (not self.use_custom_time_was_checked or self.firstloop):
            self.auto_update.setEnabled(False)
        if not self.use_custom_time.isChecked() and (self.use_custom_time_was_checked or self.firstloop):
            self.auto_update.setEnabled(True)

        if not self.auto_update.isChecked() and not self.use_custom_time.isChecked() and ((self.auto_update_was_checked or self.use_custom_time_was_checked) or self.firstloop):
            self.update_button.setEnabled(True)

        if not self.auto_update.isChecked() and not self.use_custom_time_was_checked and ((self.auto_update_was_checked or self.use_custom_time_was_checked) or self.firstloop):
            self.date_before_auto_update = datetime.date.today()
            self.time_before_auto_update = datetime.datetime.now().time()
            self.update_button.setEnabled(True)


        if (self.auto_update.isChecked() or self.use_custom_time.isChecked()) and (not self.auto_update_was_checked or self.firstloop):
            self.update_button.setEnabled(False)

        self.update()
        self.use_custom_time_was_checked = self.use_custom_time.isChecked()
        self.auto_update_was_checked = self.auto_update.isChecked()
        self.firstloop = False
        QTimer.singleShot(50, self.timerloop)

    def saveloop(self):
        print(self.jupiter.sunalt)
        print(self.jupiter.sunaz)
        print("\n\n")
        savefile.write({
            "lat": self.get_latitude(),
            "lon": self.get_longitude(),
            "elev": self.alt_input.text(),
            "date": str(self.date_input.date().toPython()),
            "time": str(self.time_input.time().toPython()),
            "timezone": self.timezone_dropdown.currentIndex(),
            "auto_update": self.auto_update.isChecked(),
            "use_custom_time": self.use_custom_time.isChecked(),
            "antenna_temp": self.antenna_temp.text(),
        })
        QTimer.singleShot(1000, self.saveloop)
