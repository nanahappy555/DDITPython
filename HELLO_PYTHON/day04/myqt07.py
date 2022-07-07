"""
가위바위보
"""
from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication
import sys
import random


# ui파일(xml형식) 연결
form_class = uic.loadUiType("myqt07.ui")[0]

# 윈도우를 띄워주는 메소드
class WindowClass(QMainWindow, form_class):
    # 생성자
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.buttonClick)
        # self.show() 메인에 쓴 myWindow.show()와 같음
        
    
    def buttonClick(self):
        mine = self.le_mine.text()
        rnd = random.randint(1,2+1)
        
        com = ""
        
        if rnd == 1:
            com = "가위"
        elif rnd ==2:
            com = "바위"
        else:
            com = "보"
        
        # 이런 소스가 좋은 이유... 직관적으로 알아볼 수 있어서 고객도 알아들을 수 있다...
       if com == "가위" and mine == "가위": result = "비김"
       if com == "가위" and mine == "바위": result = "내가 이김"
       if com == "가위" and mine == "보": result = "내가 짐"
    
       if com == "바위" and mine == "가위": result = "내가 짐"
       if com == "바위" and mine == "바위": result = "비김"
       if com == "바위" and mine == "보": result = "내가 이김"
    
       if com == "보" and mine == "가위": result = "내가 이김"
       if com == "보" and mine == "바위": result = "내가 짐"
       if com == "보" and mine == "보": result = "비김"
    
        if com.__eq__(mine):
            result = "비김"
        # 이건 가독성 떨어짐
        elif (com.__eq__("가위") and mine.__eq__("바위")) or (com.__eq__("바위") and mine.__eq__("보")) or (com.__eq__("보") and mine.__eq__("가위")):
        # elif (com.__eq__("가위") and mine.__eq__("바위")) 이건 에러남
        #     or (com.__eq__("바위") and mine.__eq__("보"))
        #     or (com.__eq__("보") and mine.__eq__("가위")):
            result = "내가 이김"
        else:
            result = "내가 짐"
            
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