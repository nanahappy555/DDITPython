import cv2

img1 = cv2.imread('Lenna.png')
blur = cv2.blur(img1,(5,5))

cv2.imshow('img1', img1)
cv2.imshow('blur', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()