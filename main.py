from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow

import sys

def add_button_label():
    print("yes yes")
    

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()
    
    window.setWindowTitle("Бауржан")
    window.setGeometry(300,250,700,700)
    
    
    # main_text = QtWidgets.QLabel(window)
    # main_text.setText("GeekCoin 150")
    # main_text.move(100,200)
    # main_text.adjustSize()
    
    button = QtWidgets.QPushButton(window)
    button.setText("ебашь жёстче")
    button.move(100,200)
    button.clicked.connect(add_button_label)
    
    window.show()
    sys.exit(app.exec_())
    
application()
    