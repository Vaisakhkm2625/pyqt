import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

         ## username_label = qtw.QLabel("Username")
         ## password_label = qtw.QLabel("Password")

         ## username_input = qtw.QLineEdit()
         ## password_input = qtw.QLineEdit()
         ## password_input.setEchoMode(qtw.QLineEdit.Password)

         ## cancel_button = qtw.QPushButton("Cancel")
         ## submit_button= qtw.QPushButton("Login")

         ## #layout = qtw.QHBoxLayout()
         ## #layout = qtw.QVBoxLayout()
         ## layout = qtw.QGridLayout()
         ## layout.addWidget(username_label,0,0)
         ## layout.addWidget(username_input,0,1)
         ## layout.addWidget(password_label,1,0)
         ## layout.addWidget(password_input,1,1)


        # with form layout
        username_input = qtw.QLineEdit()
        password_input = qtw.QLineEdit()

        layout = qtw.QFormLayout()
        layout.addRow("username",username_input)
        layout.addRow("password",password_input)

        button_widget = qtw.QWidget()
        cancel_button = qtw.QPushButton("cancel")
        submit_button = qtw.QPushButton("login")
        button_widget.setLayout(qtw.QHBoxLayout())
        button_widget.layout().addWidget(cancel_button)
        button_widget.layout().addWidget(submit_button)
        layout.addRow('',button_widget)

        self.setLayout(layout)

        self.show()


if __name__ == '__main__':
    app = qtw.QApplication([])
    w = MainWindow()
    sys.exit(app.exec_())
