"""
홀짝게임
"""
from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import sys
import random


# ui파일(xml형식) 연결
form_class = uic.loadUiType("myqt05.ui")[0]

# 윈도우를 띄워주는 메소드
class WindowClass(QMainWindow, form_class):
    # 생성자
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.buttonClick)
        self.le_mine.returnPressed.connect(self.returnPressed)
        
    def returnPressed(self):
        mine = self.le_mine.text()
        rnd = random.randint(1,2)
        
        com = ""
        
        if rnd == 1:
            com = "홀"
        else:
            com = "짝"
        
        if mine == com:
            result = "이김"
        else:
            result = "짐"
            
        self.le_com.setText(com)
        self.le_result.setText(result)
        
    
    def buttonClick(self):
        mine = self.le_mine.text()
        rnd = random.randint(1,2)
        
        com = ""
        
        if rnd == 1:
            com = "홀"
        else:
            com = "짝"
        
        if mine == com:
            result = "이김"
        else:
            result = "짐"
            
        self.le_com.setText(com)
        self.le_result.setText(result)
        
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