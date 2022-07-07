import time
class Cat:
    def __init__(self): # 생성자
        print("constructor")
    
    def cry(self):
        print("crying")
    
    def __del__(self): # 소멸자
        print("destroyer")
    
    # java의 toString
    def __str__(self):
        return "babo"

c = Cat()
c.cry()
time.sleep(4) # 4초 지연. 단위 sec
print(c)
"""
constructor
crying
4초뒤
babo
destroyer
"""