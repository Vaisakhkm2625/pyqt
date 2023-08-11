import sys
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class SearchWidget(qtw.QWidget):

    submitted = qtc.pyqtSignal(str,bool)

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
          
        search_image = qtg.QPixmap('search.png')

        self.term_input = qtw.QLineEdit()
        self.case_checkbox = qtw.QCheckBox('Case sensive')
        self.submit_button = qtw.QPushButton('Search',icon=qtg.QIcon(search_image),clicked=self.on_submit)

        self.setLayout(qtw.QFormLayout())
        self.layout().addRow(qtw.QLabel(pixmap=search_image))
        self.layout().addRow('Search term',self.term_input)
        self.layout().addRow('',self.case_checkbox)
        self.layout().addRow('',self.submit_button)

    def on_submit(self):
        term =  self.term_input.text()
        case_sensitive  = (self.case_checkbox.checkState() == qtc.Qt.Checked)
        self.submitted.emit(term,case_sensitive)


class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()

        #Main gui code
        self.textEdit = qtw.QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.show()

        # Menu bar

        menubar = self.menuBar()# returns a QMenuBar
        file_menu = menubar.addMenu('File') # returns a QMenu
        file_menu.addAction('Open',self.open_file) # returns a QAction
        file_menu.addSeparator()
        save_action = file_menu.addAction('Save')
        save_action.triggered.connect(self.save_file)
        file_menu.addAction('Quit',self.close)

        cat_menu = menubar.addMenu('Cat')
        cat_menu.addAction('cat',self.cat)

        # Tool bar

        edit_toolbar  = self.addToolBar('Edit') #QToolBar
        edit_toolbar.addAction('Copy',self.textEdit.copy)
        edit_toolbar.addAction('Paste',self.textEdit.paste)
        edit_toolbar.addAction('Cut',self.textEdit.cut)
        edit_toolbar.addAction('Undo',self.textEdit.undo)
        edit_toolbar.addAction('Redo',self.textEdit.redo)
        edit_toolbar.addAction('searchcat',self.searchCat)

        #Dockwidget
        search_dock = qtw.QDockWidget('Search')
        search_widget = SearchWidget()
        search_dock.setWidget(search_widget)

        self.addDockWidget(qtc.Qt.RightDockWidgetArea, search_dock)
        search_widget.submitted.connect(self.search)

        
    def cat(self):
        os.system('notify-send cat')
        self.textEdit.insertPlainText('cat')
        self.textEdit.insertHtml('<b>hello</b>')

    def save_file(self):
        text =self.textEdit.toPlainText()
        filename,_ = qtw.QFileDialog().getSaveFileName()
        if filename:
            with open(filename,'w') as handle:
                handle.write(text)
                self.statusBar.showMessage(f"{filename} saved")

    def search(self,term,case_sensitive=False):
        print('searching')
        if case_sensitive:
            cur = self.textEdit.find(
                term,
                qtg.QTextDocument.FindCaseSensitively
            )
        else:
            cur = self.textEdit.find(term)
        if not cur:
            self.statusBar().showMessage('No matchs',2000)

    def searchCat(self):
        cur = self.textEdit.find("cat")
        self.statusBar().showMessage(f'cats {cur}',2000)


    def open_file(self):
        filename,hello =  qtw.QFileDialog.getOpenFileName()
        if filename:
            print('hello',hello)
            with open(filename, 'r') as handle:
                text = handle.read()
            self.textEdit.clear()
            self.textEdit.insertPlainText(text)
            self.textEdit.moveCursor(qtg.QTextCursor.Start)
            self.statusBar().showMessage(f'Editing {filename}',2000)


        
if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec_())
