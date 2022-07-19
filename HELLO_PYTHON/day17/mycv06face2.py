import cv2
#얼굴찾아서 다른 이미지로 대체하기

# haarcascade 불러오기
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

img1 = cv2.imread('startup.png')
imggray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
face = cv2.imread('face.png')
facegray = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
ret, face_mask = cv2.threshold(facegray, 240, 255, cv2.THRESH_BINARY)

face_mask_inv = cv2.bitwise_not(face_mask)

#얼굴찾기
faces = face_cascade.detectMultiScale(imggray, 1.3, 5)
for (x, y, w, h) in faces:
    # 넣고 싶은 위치에 합성할 이미지의 크기만큼 배경 이미지를 잘라냄
    height, width = imggray.shape[:2]
    img_cut = img1[0:height, 0:width]
    
    # 배경 이미지에는 로고 들어갈 위치 삭제
    # 로고에는 로고만 냄기고 배경 삭제
    img01 = cv2.bitwise_and(face, face, mask=face_mask_inv)
    img02 = cv2.bitwise_and(img_cut, img_cut, mask=face_mask)
      
    tmp = cv2.add(img01, img02)
    img1[0:height, 0:width] = tmp
    # cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 0, 255), 2)
    
# print("img1",img1)
# print("imggray",imggray)

cv2.imshow('image1', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()