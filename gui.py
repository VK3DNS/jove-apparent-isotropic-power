from handler import run
import sys
import qapp
from PySide6.QtWidgets import QApplication, QMainWindow

communicate, values, rx, tx, calc = run()
print(values)

app = QApplication(sys.argv)
window = qapp.MainWindow(communicate, values, rx, tx, calc)
window.show()
app.exec()

print('somethikjkljkljjk.hkljlkjklndg died')