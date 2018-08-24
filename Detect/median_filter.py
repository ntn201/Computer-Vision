import cv2
import numpy as np
def median_filter3(row,col,gray4filter):
    temp = []
    for i in range(row-1,row+2):
        for j in range(col-1,col+2):
            temp.append(gray4filter[i][j])
    temp.sort()
    return temp[round(len(temp)/2)]
if __name__ == "__main__":
    img = cv2.imread("Image\\horse.jpg")

    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    cv2.imshow("Image",gray)
    gray4filter = gray.copy()
    rows = gray4filter.shape[0]
    cols = gray4filter.shape[1]
    gray_new = gray4filter.copy()





    for i in range(1,rows-1):
        for j in range(1,cols-1):
            gray_new[i][j] = median_filter3(i,j,gray4filter)

    cv2.imshow("After filter",gray_new)
    cv2.waitKey()
