from handler import run
import sys
import qapp
import time
import threading, asyncio
from PySide6.QtWidgets import QApplication, QMainWindow

communicate, values, rx, tx, calc = run()

app = QApplication(sys.argv)
window = qapp.MainWindow(communicate, values, rx, tx, calc)
window.timerloop()
window.saveloop()
window.show()

app.exec()