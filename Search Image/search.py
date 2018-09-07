import glob
import cv2
import numpy as np

def load_image():
    img1 = glob.glob("Image/*.jpg")
    img2 = glob.glob("Image/*.png")
    res = img1 + img2
    return res

img_name_list = load_image()

img_list = []

for i in img_name_list:
    img = cv2.imread(i)
    img_list.append(img)

img_search = cv2.imread("Image/img.png")

cv2.imshow("Hihi",img_search)
gray = cv2.cvtColor(img_search,cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()
kp1,des1 = sift.detectAndCompute(gray,None)
newImg = img_search.copy()

match_list = []
bf = cv2.BFMatcher_create()

for img in img_list:
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    kp2,des2 = sift.detectAndCompute(img_gray,None)
    matches = bf.knnMatch(des1,des2,k = 2)
    good = []
    for m,n in matches:
        if m.distance < 0.4*n.distance:
            good.append(m)
    match_list.append(len(good))

if max(match_list) > 0.4*len(kp1):
    cv2.imshow("Found Img",img_list[match_list.index(max(match_list))])
else:
    print("Ko co anh nay")

cv2.waitKey()
