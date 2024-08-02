from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QSlider, QApplication, QLabel, QLineEdit, QPushButton, QTextEdit, QDateEdit, QTimeEdit, QCheckBox
import sys
from PySide6.QtCore import Qt
import get_lat_long_dist
import datetime

print(datetime.datetime.now())


class MainWindow(QMainWindow):
    def __init__(self, communicate, values, rx, tx, calc):
        super().__init__()

        self.jupiter = get_lat_long_dist.JupiterValues()

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
        self.lat_input.setText(str(self.jupiter.lat))
        layout.addWidget(self.lat_input)

        self.lon_label = QLabel("Longitude:")
        layout.addWidget(self.lon_label)
        self.lon_input = QLineEdit()
        self.lon_input.setText(str(self.jupiter.lon))
        layout.addWidget(self.lon_input)

        self.custom_time_label = QLabel("Custom Date & Time:")
        layout.addWidget(self.custom_time_label)
        self.date_input = QDateEdit()
        layout.addWidget(self.date_input)
        self.time_input = QTimeEdit()
        layout.addWidget(self.time_input)

        self.use_custom_time_label = QLabel("Use Custom Date & Time:")
        layout.addWidget(self.use_custom_time_label)
        self.use_custom_time = QCheckBox()
        self.use_custom_time.stateChanged.connect(self.update)
        layout.addWidget(self.use_custom_time)

        self.use_daylight_savings_label = QLabel("Daylight Savings Time:")
        layout.addWidget(self.use_daylight_savings_label)
        self.use_daylight_savings = QCheckBox()
        self.use_daylight_savings.stateChanged.connect(self.update)
        layout.addWidget(self.use_daylight_savings)

        self.antenna_temp_label = QLabel("Antenna Temp:")
        layout.addWidget(self.antenna_temp_label)
        self.antenna_temp = QLineEdit()
        self.antenna_temp.setText("1")
        layout.addWidget(self.antenna_temp)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.output_box = QTextEdit()
        self.output_box.setReadOnly(True)
        layout.addWidget(self.output_box)

        self.update_button = QPushButton("Update")
        layout.addWidget(self.update_button)
        self.update_button.clicked.connect(self.update)

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

    def update(self):
        self.jupiter.lat = self.get_latitude()
        self.jupiter.lon = self.get_longitude()

        date = self.date_input.date().toPython()
        time = self.time_input.time().toPython()
        custom_datetime = datetime.datetime.combine(date, time)
        self.jupiter.update_values(datetime.datetime.now() if not self.use_custom_time.isChecked() else custom_datetime)

        num = float(str(self.jupiter.distance)[:-3])*10**7

        self.communicate.set_AuD.emit(num)
        self.communicate.get_values.emit()

        self.calc.K = float(self.antenna_temp.text())

        self.calc.calculateisotropicpower()

        isopower = self.values["IsotropicPower"]

        AEDT = "AEDT"
        AEST = "AEST"

        self.output_box.setPlainText(f"Distance: {self.jupiter.distance}\nRa: {self.jupiter.ra}\nDec: {self.jupiter.dec}\n\nTime zone: {AEDT if self.use_daylight_savings.isChecked() else AEST}\n\nApparent Power: {isopower}")

    def get_longitude(self):
        return self.lon_input.text()

    def get_latitude(self):
        return self.lat_input.text()
