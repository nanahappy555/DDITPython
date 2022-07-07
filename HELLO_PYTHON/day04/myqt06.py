"""
로또
"""
import random
import sys

from PyQt5 import uic
from PyQt5.Qt import QMainWindow, QApplication


# ui파일(xml형식) 연결
form_class = uic.loadUiType("myqt06.ui")[0]

# 윈도우를 띄워주는 메소드
class WindowClass(QMainWindow, form_class):
    # 생성자
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.pb.clicked.connect(self.buttonClick)
        # self.pb.clicked.connect(self.sem)
        # self.show() 메인에 쓴 myWindow.show()와 같음
    
    """
    for idx,i in enumerate(arr) :
    print(idx,i)
    idx+=1
    """
    # 배열의 길이 : len(배열이름)
    def buttonClick(self):
        lottos = []
        
        while len(lottos) < 6:
            a = random.randint(1,45)
            if a not in lottos:
                lottos.append(a)
        
        print("lottos",lottos[0])
        print("lottos",lottos[1])
        print("lottos",lottos[2])
        print("lottos",lottos[3])
        print("lottos",lottos[4])
        print("lottos",lottos[5])
        
        self.lbl1.setText(lottos[0])
        self.lbl2.setText(lottos[1])
        self.lbl3.setText(lottos[2])
        self.lbl4.setText(lottos[3])
        self.lbl5.setText(lottos[4])
        self.lbl6.setText(lottos[5])

    
    def sem(self):    
        arr6 = [
                "1","2","3","4","5", "6"
        ]
        for i in range(10):
            rnd = int(random.random()*len(arr6))
            a = arr6[rnd]
            b = arr6[0]
            arr6[0] = a
            arr6[rnd] = b
            # temp = arr6[rnd]
            # arr6[rnd] = arr6[0]
            # arr6[0] = temp
        
            # print(rnd)
        
            self.lbl1.setText(arr6[0])
            self.lbl2.setText(arr6[1])
            self.lbl3.setText(arr6[2])
            self.lbl4.setText(arr6[3])
            self.lbl5.setText(arr6[4])
            self.lbl6.setText(arr6[5])
        
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