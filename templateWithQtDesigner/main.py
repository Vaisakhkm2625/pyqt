# https://www.youtube.com/watch?v=M7UdAX77kpY
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self,*arg,**kwargs):
        super().__init__(*arg,**kwargs)
        # code goes here

        # -- self.button = qtw.QPushButton('click me')

        # code ends here
        self.show()


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    w = MainWindow()

    sys.exit(app.exec_())
