import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon, QPushButton, QRect, QMessageBox
from sklearn.semi_supervised.tests import test_self_training
from Cython.Compiler.Naming import self_cname
from conda.common._logic import TRUE

form_class = uic.loadUiType("omok03.ui")[0]


class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.flagWb = True # True면 흰돌, False면 검은돌
        self.flagIng = True # 게임이 진행중이면 True
        
        self.goSize = 19 #바둑판 사이즈
        
        self.arr2D = []
        for i in range(self.goSize):
            line = []
            for j in range(self.goSize):
                line.append(0)
            self.arr2D.append(line)
    
        # self.arr2D = [ # 이 로직의 코어
        #     [0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0,  0,0,0,0,0],
        #
        #     [0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0,  0,0,0,0,0],
        #     [0,0,0,0,0,  0,0,0,0,0]
        # ]
        self.pb2D = [] # btn을 세팅할 배열 선언
        self.setupUi(self)
        
        for i in range(self.goSize): # i == y
            line = [] # for문이 돌아갈 때 라인 19개가 생긴다
            for j in range(self.goSize): # j == x
                btn = QPushButton('',self)
                btn.setIcon(QtGui.QIcon("0.png"))
                btn.setGeometry(j*40,i*40,40,40) # x, y, width, height
                btn.setIconSize(QtCore.QSize(40,40))
                btn.setToolTip("{},{}".format(i,j))
                btn.clicked.connect(self.myclick)
                line.append(btn) #line에 19개넣기 19
            self.pb2D.append(line) #pb2D에 line 19개 넣기 19x19
        
        
        self.myrender()
        
        self.pbReset.clicked.connect(self.gameReset)
        
        self.show()
        QMessageBox.information(self, '게임 시작', "●●●오목게임을 시작합니다○○○")
    
    # 리셋버튼 누르면 1.모든 돌 제거(arr2D 0) 2.다시 돌을 놓게(flagIng) 3.다시 흰돌부터 놓게(flagWb)
    def gameReset(self):
        for i in range(self.goSize):
            for j in range(self.goSize):
                self.arr2D[i][j] = 0
        
        self.flagIng = True
        self.flagWb = True
        
        QMessageBox.information(self, '게임 시작', "게임이 초기화 됐습니다. \n 흰돌부터 시작!")
        
        self.myrender()
        
    
    def myrender(self):
        # arr2D배열에 있는 숫자에 따라 pb2D에 흰돌 검은돌 세팅
        # 0이면 0.png, 1이면 1.png, 2면 2.png
        
        for i in range(self.goSize):
            for j in range(self.goSize):
                if self.arr2D[i][j] == 0:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("0.png"))
                    
                if self.arr2D[i][j] == 1:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("1.png"))
                    
                if self.arr2D[i][j] == 2:
                    self.pb2D[i][j].setIcon(QtGui.QIcon("2.png"))
            
    
    def myclick(self):
        # 게임이 종료되면 리턴됨
        # 이 코드는 왜 여기? 필요한 정보는 전역변수에서 받아오니까 최대한 위에 둔다.
        # 다른 코드 필요없고 리턴만 할건데 아래로 내려가봤자 메모리만 씀 
        if not self.flagIng:
            return
        
        str_ij = self.sender().toolTip() # 클릭한 버튼의 툴팁(좌표)가져오기
        arr_ij = str_ij.split(',') # 좌표가 콤마(,)를 기준으로 잘라서 배열로 반환됨 ['i', 'j']
        i = int(arr_ij[0]) # 'i'
        j = int(arr_ij[1]) # 'j'
        
        # 배열에 이미 1or2의 값이 들어가 있으면 (=돌이 놓여져 있으면) 돌을 놓을 수 없게 return
        # 이 코드는 왜 여기? 최대한 위에 두는데 i,j는 필요해서 여기 둠
        if self.arr2D[i][j] > 0 :
            return 
        
        stone = -1 # 
        # 코어(배열)에 데이터를 변경함
        if self.flagWb :
            # self.arr2D[i][j] = 1 # 코어(배열)에 데이터를 변경함
            self.arr2D[i][j] = 1
            stone = 1
        else :
            self.arr2D[i][j] = 2
            stone = 2
        
        up = self.checkUp(i,j,stone) # 위
        dw = self.checkDown(i,j,stone) # 아래
        ri = self.checkRi(i,j,stone) # 오
        le = self.checkLe(i,j,stone) # 왼
        
        ur = self.checkUR(i,j,stone)
        ul = self.checkUL(i,j,stone)
        dr = self.checkDR(i,j,stone)
        dl = self.checkDL(i,j,stone)
        
        d1 = up + dw + 1
        d2 = ur + dl + 1
        d3 = le + ri + 1
        d4 = ul +dr + 1
        
        self.myrender() # myrender 호출

        #
        if d1 == 5 or d2 == 5 or d3 == 5 or d4 == 5 :
            self.flagIng = False # 여기 둬야 여러번 안쓴다
            print("게임종료")
            wWin = "흰돌 승리"
            bWin = "검은돌 승리"
            
            self.arr2D[i][j]
            
            # stone이 아니라 flagWb로 쓰는 이유?
            # flagWb가 코어라서 stone을 보고 짰을 경우 stone이 바뀌면 꼬일수있다.
            if self.flagWb: 
                QMessageBox.information(self, '게임 결과', wWin)
                return  
            else: 
                QMessageBox.information(self, '게임 결과', bWin)  
                return  
            
        
        self.flagWb = not self.flagWb # True일 때 False로 바꿈 / False일 때 True로 바꿈

    # 우상 돌 갯수 체크
    def checkUR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i<0: 
                    return cnt
                if j<0: 
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt # 오류났을 때 cnt를 증가시키지 않고 지금까지의 cnt가 리턴됨
        
    # 좌상 돌 갯수 체크
    def checkUL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                j -= 1
                if i<0: 
                    return cnt
                if j<0: 
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt # 오류났을 때 cnt를 증가시키지 않고 지금까지의 cnt가 리턴됨
        
    # 우하 돌 갯수 체크
    def checkDR(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j += 1
                if i<0: 
                    return cnt
                if j<0: 
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt # 오류났을 때 cnt를 증가시키지 않고 지금까지의 cnt가 리턴됨
        
    # 좌하 돌 갯수 체크
    def checkDL(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                j -= 1
                if i<0: 
                    return cnt
                if j<0: 
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt # 오류났을 때 cnt를 증가시키지 않고 지금까지의 cnt가 리턴됨
        
    # 왼쪽 돌 갯수 체크
    def checkLe(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j -= 1
                if i<0: 
                    return cnt
                if j<0: 
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt # 오류났을 때 cnt를 증가시키지 않고 지금까지의 cnt가 리턴됨
        
    # 오른쪽 돌 갯수 체크
    def checkRi(self,i,j,stone):
        cnt = 0
        try:
            while True:
                j += 1
                if i<0: 
                    return cnt
                if j<0: 
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt # 오류났을 때 cnt를 증가시키지 않고 지금까지의 cnt가 리턴됨
        
    # 위쪽 돌 갯수 체크
    def checkUp(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i -= 1
                if j<0: 
                    return cnt                
                if i<0: # 맨 밑에 찍고 맨 위에 찍었을 경우 i=-1에 돌이 있어서 arr2D[-1][j]에 있는 돌까지 카운트해버리고 돌갯수 1이 나온다. python배열의 특징(-는 뒤에서부터 돈다)
                    return cnt
                
                if self.arr2D[i][j] == stone:
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt # 오류났을 때 cnt를 증가시키지 않고 지금까지의 cnt가 리턴됨
            
    # 아래쪽 돌 갯수 체크
    def checkDown(self,i,j,stone):
        cnt = 0
        try:
            while True:
                i += 1
                if j<0: 
                    return cnt               
                if i<0: 
                    return cnt
                
                if self.arr2D[i][j] == stone: # 맨 밑에 찍으면 idx값이 배열길이를 넘어서서 에러 뜸
                    cnt += 1
                else:
                    return cnt
        except:
            return cnt # 오류났을 때 cnt를 증가시키지 않고 지금까지의 cnt가 리턴됨
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    window = MainClass() 
    app.exec_()