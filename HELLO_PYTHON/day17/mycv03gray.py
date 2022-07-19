import cv2

img1 = cv2.imread('r.png')
dst = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
print("dst",dst)
cv2.imshow('dst', dst)


cv2.waitKey(0)
cv2.destroyAllWindows()


# dst [[123  93]
#  [ 94  91]
#  [ 94  91]]
#
# img1 [[[ 77  72 240]        129
#
#   [ 37  31 237]]        101
#
#  [[ 39  31 237]         102
#   [ 36  28 237]]        100
#
#  [[ 40  32 237]         103
#   [ 36  28 237]]]       100