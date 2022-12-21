from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def application():
    app =   QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("PyQT5 Window")
    window.setGeometry(300, 250, 700, 500)
    

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Alikhan")

    window.show()
    sys.exit(app.exec_())

application()