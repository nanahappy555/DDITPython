import cv2

img1 = cv2.imread('startup.png')
x = 330
y = 100
w = 500
h = 500

crop = img1[y:y+h, x:x+w] #슬라이싱

print("img1",img1)
print("crop",crop)
cv2.imshow('img1', img1)
cv2.imshow("crop",crop)

cv2.waitKey(0)
cv2.destroyAllWindows()