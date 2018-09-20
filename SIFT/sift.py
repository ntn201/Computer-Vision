import cv2
import numpy as np

# Load image insert
img_ist = cv2.imread("Image/SM5_EN_13.png")

img = cv2.imread("Image/image.jpg")
#cv2.imshow("Image",img)
cv2.waitKey(1)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#cv2.imshow("Gray",gray)


# Find keypoints

sift = cv2.xfeatures2d.SIFT_create()
kp1, des1 = sift.detectAndCompute(gray,None)

newImg = img.copy()
cv2.drawKeypoints(img,kp1,newImg)

#cv2.imshow("Keypoints",newImg)
mask = np.ones_like(img,dtype = np.float32)

cap = cv2.VideoCapture(0)

while True:
    ret,img2 = cap.read()


    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    #cv2.imshow("Gray2",gray2)

    cv2.waitKey(1)

    sift2 = cv2.xfeatures2d.SIFT_create()
    kp2, des2 = sift.detectAndCompute(gray2,None)

    #Matching image by brute force algorithm
    bf = cv2.BFMatcher_create()
    matches = bf.knnMatch(des1,des2,k = 2)
    mtcImg = cv2.drawMatchesKnn(img,kp1,img2,kp2,matches,None)
    
    #Choose good point
    good = []
    for m,n in matches:
        if m.distance < 0.3*n.distance:
            good.append(m)
    # Find homography
    src_points = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1,1,2)
    dst_points = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1,1,2)

    M, H = cv2.findHomography(src_points,dst_points)
    w = gray.shape[1]
    h = gray.shape[0]
    pattern = cv2.resize(img_ist,(w,h))

    ncorners = np.float32([[0,0],[w-1,0],[w-1,h-1],[0,h-1]]).reshape(-1,1,2)
    if M is None:
        pass
    else:
        newpts = cv2.perspectiveTransform(ncorners,M)
        cv2.polylines(img2, np.int32([newpts]),True,(0,0,255),4)
        # Insert image
        blendmask = cv2.warpPerspective(mask,M,(img2.shape[1],img2.shape[0]))
        newPattern = cv2.warpPerspective(pattern,M,(img2.shape[1],img2.shape[0]))
        img_result = img2*(1 - blendmask) + newPattern
        img_result = cv2.convertScaleAbs(img_result)
        cv2.imshow("Haha",img_result)
        cv2.imshow("Hihi",img2)


    goodMatchImg = cv2.drawMatches(img,kp1,img2,kp2,good,None)
    cv2.imshow("Good Match",goodMatchImg)
    key = cv2.waitKey(1)
    if key&0xFF == ord("q"):
        break

  
