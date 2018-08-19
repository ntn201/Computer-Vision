import cv2
import numpy

img = cv2.imread("Image\contour1.jpg")


B,G,R = cv2.split(img)
img2 = cv2.bitwise_and(B,R)
img2 = cv2.bitwise_not(img2)


cv2.imshow("Blue",B)
cv2.imshow("Green",G)
cv2.imshow("Red",R)
cv2.imshow("Red and Blue",img2)

ret, imgROI = cv2.threshold(img2,50,255,cv2.THRESH_BINARY)


# Find contour
N, contours, hierachy = cv2.findContours(imgROI,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

for i in contours:
    cv2.drawContours(imgROI,i,-1,(0,255,0),3)
    nedges = cv2.approxPolyDP(i,5,True)
    # Get perimeter
    peri = cv2.arcLength(i,True)
    area = cv2.contourArea(i,True)
    #print(nedges)
    print(len(nedges),peri,area)
    if len(nedges) == 3
        x = nedges[0][0][0]
        y = nedges[0][0][1]
        cv2.putText(img,"Triangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))
    if len(nedges) == 4:
        x = nedges[0][0][0]
        y = nedges[0][0][1]
        cv2.putText(img,"Rectangle",(x,y),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0))

cv2.imshow("Contours",img)
cv2.waitKey()
