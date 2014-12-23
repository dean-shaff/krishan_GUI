import os 
import sys
from PyQt4 import  QtCore, QtGui


class Main_Window(QtGui.QMainWindow):

    def __init__(self,parent=None):
        super(Main_Window,self).__init__(parent)
        self.initwindow()

    def initwindow(self):

        self.widget = Example(self)
        self.setCentralWidget(self.widget)
        self.setGeometry(300,300,600,600)
        self.setWindowTitle("Krishan's Poem Generator")
        self.show()


class Example(QtGui.QWidget):
    
    def __init__(self,parent):
        super(Example, self).__init__(parent)
        
        self.initUI()
        
    def initUI(self):      

        self.btn = QtGui.QPushButton('Dialog', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)
        
        self.le = QtGui.QLineEdit(self)
        self.le.move(130, 22)
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Input dialog')
        self.show()
        
    def showDialog(self):
        
        input_box = QtGui.QInputDialog()
        input_box.setOkButtonText("Sent")
        ok = input_box.exec_()
        text = input_box.getText()
        # text, ok = input_box.getText(self, "Send Email", "Email Address:")
        
        if ok:
            self.le.setText(str(text))
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Main_Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()