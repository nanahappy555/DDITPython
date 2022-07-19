import cv2

src = cv2.imread('Lenna.jpg')
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

dst_01 = mosaic(src)
cv2.imwrite('C:/Users/Administrator/Desktop/python/origin/face_mosaic_01.jpg', dst_01)

dst_005 = mosaic(src, ratio=0.05)

cv2.imwrite('C:/Users/Administrator/Desktop/python/origin/face_mosaic_005.jpg', dst_005)