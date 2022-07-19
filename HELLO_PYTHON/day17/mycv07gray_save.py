import cv2

img1 = cv2.imread('Lenna.png')
gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

cv2.imwrite('Lenna.jpg', gray)
print("img1",img1)

cv2.imshow('image1gray', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()