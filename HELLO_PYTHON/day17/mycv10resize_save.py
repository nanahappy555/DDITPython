import cv2

img1 = cv2.imread('startup.png')

resize = cv2.resize(img1, (200,100))


cv2.imshow('img1', resize)


cv2.waitKey(0)
cv2.destroyAllWindows()