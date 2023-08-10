import os
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

    

class MainWindow(qtw.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # with form layout
        self.username_input = qtw.QLineEdit()
        self.password_input = qtw.QLineEdit()

        self.Layout = qtw.QFormLayout()
        self.Layout.addRow("username",self.username_input)
        self.Layout.addRow("password",self.password_input)

        self.cancel_button = qtw.QPushButton("cancel")
        self.submit_button = qtw.QPushButton("login")

        button_widget = qtw.QWidget()

        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(self.cancel_button)
        button_widget.layout().addWidget(self.submit_button)
        self.Layout.addRow('',button_widget)

        self.setLayout(self.Layout)

        self.username_input.textChanged.connect(self.set_button_text)
        self.cancel_button.clicked.connect(self.close)
        self.submit_button.clicked.connect(self.authenticate)

        self.show()

    def set_button_text(self, text):
        if text:
            self.submit_button.setText(f'login as {text}')
        else:
            self.submit_button.setText('login')

    def authenticate(self):
        user = self.username_input.text()
        passw = self.password_input.text()

        if  user=='user' and passw=='pass':
            qtw.QMessageBox.information(self,'login success','you logged in')
        else:
            qtw.QMessageBox.information(self,'login failed','get the hell out')

if __name__ == '__main__':
    app = qtw.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())
