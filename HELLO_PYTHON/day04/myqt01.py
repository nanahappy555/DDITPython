import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("omok01.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.pb.clicked.connect(self.myclick)
        # self.lbl.clicked.connect(self.myclick)
        self.show()
        
    def myclick(self):   
        self.lbl.setPixmap(QtGui.QPixmap("1.png"))
        print("myclick")
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()