# 홀짝을 입력하시오
# 나 홀
# 컴 홀
# 결과 이김

# 나 홀
# 컴 짝
# 결과 짐

# 컴퓨터가 뽑은 걸 맞추면 이김

import random 
#random.random()같은 형식일때는
# #import문에 from이 들어가면 에러난다

me = input("홀/짝을 입력하시오 : ")
num = random.randint(1,2) # 1부터 2까지


com = ""
if num == 1 :
    com = "홀"
else :
    com = "짝"

print("나 : "+me)
print("컴 : "+com)

if (com == me):
    print("결과 : 이김")
else :
    print("결과 : 짐")

""" 쌤 필기
com = ""
mine = ""
result = ""

mine = input("홀/짝을 고르시오")

rnd = random.random()

if rnd > 0.5:
    com = "홀"
else:
    com = "짝"

if com == mine:
    result = "이김"
else:
    result = "짐"

print("나 ",mine)
print("컴 ",com)
print("결과 ",result)

"""