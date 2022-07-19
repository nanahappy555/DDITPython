import cv2

src = cv2.imread('Lenna.png')
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

dst_area = mosaic_area(src, 100, 100, 100, 100)

cv2.imshow('Lenna.png', dst_area)

cv2.waitKey(0)
cv2.destroyAllWindows()