import cv2

img1 = cv2.imread('Lenna.png')
img2 = cv2.imread('Lenna.png', 1)
img3 = cv2.imread('Lenna.png', cv2.IMREAD_COLOR)

print("img1",img1)
print("img1",type(img1))
print("img2",type(img2))
print("img3",type(img3))

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()