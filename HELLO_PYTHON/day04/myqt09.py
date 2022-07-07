"""
전화기
"""
from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication, QMessageBox
import sys


# ui파일(xml형식) 연결
form_class = uic.loadUiType("myqt09.ui")[0]

# 윈도우를 띄워주는 메소드
class WindowClass(QMainWindow, form_class):
    # 생성자
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.result = ""
        
        self.pb1.clicked.connect(self.pb1Click)
        self.pb2.clicked.connect(self.pb2Click)
        self.pb3.clicked.connect(self.pb3Click)
        self.pb4.clicked.connect(self.pb4Click)
        self.pb5.clicked.connect(self.pb5Click)
        self.pb6.clicked.connect(self.pb6Click)
        self.pb7.clicked.connect(self.pb7Click)
        self.pb8.clicked.connect(self.pb8Click)
        self.pb9.clicked.connect(self.pb9Click)
        self.pb0.clicked.connect(self.pb0Click)
        # self.pb_call.clicked.connect(self.pbCallClick)
        # self.pb1.clicked.connect(self.myclick)
        # self.pb_call.clicked.connect(self.mycall)
        # self.show() #메인에 쓴 myWindow.show()와 같음
        
    def myclick(self):   
        # print(self.sender().text()) #call 출력
        # print(self.sender()( # <PyQt5.QtWidgets.QPushButton object at 0x000002138BF545E0>
        str_new = self.sender().text()
        str_old = self.le.text()
        self.le.setText(str_old+str_new)
        
    def mycall(self):   
        str_tel = self.le.text()
        QMessageBox.question(self, 'calling', str_tel, QMessageBox.Yes, QMessageBox.NoButton)
        
        
    def pb1Click(self): 
        a = self.pb1.text()  
        self.result += a
        
        self.le.setText(self.result)
        
    def pb2Click(self): 
        a = self.pb2.text()  
        self.result += a
        
        self.le.setText(self.result)
        
    def pb3Click(self): 
        a = self.pb3.text()  
        self.result += a
        
        self.le.setText(self.result)
        
    def pb4Click(self): 
        a = self.pb4.text()  
        self.result += a
        
        self.le.setText(self.result)
        
    def pb5Click(self): 
        a = self.pb5.text()  
        self.result += a
        
        self.le.setText(self.result)
        
    def pb6Click(self): 
        a = self.pb6.text()  
        self.result += a
        
        self.le.setText(self.result)
        
    def pb7Click(self): 
        a = self.pb7.text()  
        self.result += a
        
        self.le.setText(self.result)
        
    def pb8Click(self): 
        a = self.pb8.text()  
        self.result += a
        
        self.le.setText(self.result)
        
    def pb9Click(self): 
        a = self.pb9.text()  
        self.result += a
        
        self.le.setText(self.result)
        
    def pb0Click(self): 
        a = self.pb0.text()  
        self.result += a
        
        self.le.setText(self.result)
    
    def pbCallClick(self):
        print("calling...")
        msg = self.le.text() + "\n calling..."
        QMessageBox.information(self, 'Information Title', msg)   
        

# 메인메소드?
if __name__ == "__main__":
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()