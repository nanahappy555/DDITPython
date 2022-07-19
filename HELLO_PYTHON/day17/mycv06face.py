import cv2
#얼굴찾아서 테두리 빨갛게 테두리. 3개이상이면 성공

# haarcascade 불러오기
cascade_file = 'cascade/haarcascade_frontalface_alt2.xml'
cascade = cv2.CascadeClassifier(cascade_file)

img = cv2.imread('startup.png')
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face_list = cascade.detectMultiScale(imggray, minSize = (100,100)) 

#얼굴찾기
for (x, y, w, h) in face_list:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
# print("img1",img1)
# print("imggray",imggray)

cv2.namedWindow('img', cv2.WINDOW_NORMAL)
cv2.imshow('img', img)
cv2.imwrite('temp.jpg', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()