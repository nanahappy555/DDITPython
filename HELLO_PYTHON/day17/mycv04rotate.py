import cv2

img1 = cv2.imread('startup.png')

# 중심 계산
(h, w) = img1.shape[:2] # 이미지 크기 구하기
(cX, cY) = (w // 2, h // 2) # 중심좌표

#이미지 중심을 중심으로 45도 회전
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
imgrotated_45 = cv2.warpAffine(img1, M, (w,h))

print("img1",img1)
cv2.imshow('img1', img1)
cv2.imshow('imgrotated_45', imgrotated_45)


cv2.waitKey(0)
cv2.destroyAllWindows()
