"""
x와 y 사이의 의 z배수의 합
"""
from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import sys


# ui파일(xml형식) 연결
form_class = uic.loadUiType("myqt0a.ui")[0]

# 윈도우를 띄워주는 메소드
class WindowClass(QMainWindow, form_class):
    # 생성자
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.buttonClick)
        # self.show() 메인에 쓴 myWindow.show()와 같음
        
    
    def buttonClick(self):
        x = int(self.le1.text())
        y = int(self.le2.text())
        z = int(self.le3.text())
        
        result = 0
        
        for i in range(x,y+1):
            if(i % z == 0):
                result += i
        
        self.le_result.setText(str(result))
        

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