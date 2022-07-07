"""
a + b = 버튼 클릭 시 출력
"""
from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import sys



# ui파일(xml형식) 연결
form_class = uic.loadUiType("myqt03.ui")[0]

# 윈도우를 띄워주는 메소드
class WindowClass(QMainWindow, form_class):
    # 생성자
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.buttonClick)
        # self.show() 메인에 쓴 myWindow.show()와 같음
        
    # 버튼 클릭 이벤트
    def buttonClick(self):
        a = self.le1.text()
        b = self.le2.text()
        
        aa = int(a)
        bb = int(b)
        
        sum = aa + bb
        
        self.le3.setText(str(sum))
        
        

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