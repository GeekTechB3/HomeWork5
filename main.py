from PyQt5 import  QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys 

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle("PyQt window")
    window.setGeometry(300, 250, 500, 500)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("GeekCoin 150KGS")

    window.show()
    sys.exit(app.exec_())

application()    