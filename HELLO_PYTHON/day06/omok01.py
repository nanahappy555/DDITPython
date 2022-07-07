import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton, QRect

form_class = uic.loadUiType("omok01.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.flagWb = False
        self.setupUi(self)
        
        for j in range(10):
            for i in range(10):
                btn = QPushButton('',self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setGeometry(i*40,j*40,40,40) # x, y, width, height
                btn.setIconSize(QtCore.QSize(40,40))
                btn.clicked.connect(self.myclick)
        
        self.show()
    
    def myclick(self):   
        # self.sender() 자기자신 가져옴
        
        if self.flagWb :
            self.sender().setIcon(QtGui.QIcon("1.png"))
        else :
            self.sender().setIcon(QtGui.QIcon("2.png"))
        
        self.flagWb = not self.flagWb # False일 때 True로 바꿈
        
        # btn.setIcon(QIcon("1.png"))
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()