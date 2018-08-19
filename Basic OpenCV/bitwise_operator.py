import cv2
img1 = cv2.imread("im1.jpg")
img2 = cv2.imread("im2.png")



rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

img1_bg = cv2.bitwise_xor(roi,roi, mask    = mask_inv)

cv2.imshow('res',img1_bg)
# cv2.imshow("mask",mask)
# cv2.imshow("img2gray",img2gray)
cv2.imshow("mask_inv", mask_inv)

cv2.waitKey(0)
cv2.destroyAllWindows()