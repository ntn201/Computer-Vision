import cv2
import numpy as np

img = cv2.imread("manga.png")
#img2 = cv2.imread("Image/SM5_EN_136.png")
cv2.imshow("Image",img)
cv2.waitKey(1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#cv2.imshow("Gray",gray)


# Find keypoints

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray,None)

newImg = img.copy()
cv2.drawKeypoints(img,kp1,newImg)

cv2.imshow("Keypoints",newImg)


cap = cv2.VideoCapture(0)

while True:
    ret,img2 = cap.read()


    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    #cv2.imshow("Gray2",gray2)

    #cv2.waitKey(1)

    sift2 = cv2.xfeatures2d.SIFT_create()
    kp2, des2 = sift.detectAndCompute(gray2,None)

    # Matching image by brute force algorithm
    bf = cv2.BFMatcher_create()
    matches = bf.knnMatch(des1,des2,k = 2)
    mtcImg = cv2.drawMatchesKnn(img,kp1,img2,kp2,matches,None)
    
    #Choose good point
    good = []
    for m,n in matches:
        if m.distance < 0.7*n.distance:
            good.append(m)
    goodMatchImg = cv2.drawMatches(img,kp1,img2,kp2,good,None)

    cv2.imshow("Good Match",goodMatchImg)

    key = cv2.waitKey(1)
    
    if key&0xFF == ord("q"):
        break

  
