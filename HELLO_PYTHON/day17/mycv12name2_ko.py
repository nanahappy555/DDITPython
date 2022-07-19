import cv2

img1 = cv2.imread('startup.png')
print("img1",img1.shape) # 이미지 사이즈 확인
# (853, 1280, 3)

text = "SUZY"
org = (470,200)
# 폰트 지정
font =  cv2.FONT_HERSHEY_SIMPLEX
 
# 이미지에 글자 합성하기
img = cv2.putText(img1, text, org, font,1,(255,0,0),2)

cv2.imshow('img1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()