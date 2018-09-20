import glob
import cv2
import numpy as np

def load_image():
    img1 = glob.glob("Image/*.jpg")
    img2 = glob.glob("Image/*.png")
    res = img1 + img2
    return res


img_name_list = load_image()
video_list = glob.glob("Image/*.mp4")

cap = cv2.VideoCapture(0)

sift = cv2.xfeatures2d.SIFT_create()
bf = cv2.BFMatcher_create()

while True:
    ret,img_search = cap.read()
    gray = cv2.cvtColor(img_search,cv2.COLOR_BGR2GRAY)
    kp1,des1 = sift.detectAndCompute(gray,None)
    match_list = []
    for img in img_list:
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        kp2,des2 = sift.detectAndCompute(img_gray,None)
        matches = bf.knnMatch(des1,des2,k = 2)
        good = []
        for m,n in matches:
            if m.distance < 0.4*n.distance:
                good.append(m)
        match_list.append(len(good))    


