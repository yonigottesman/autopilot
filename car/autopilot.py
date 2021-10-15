import cv2
import numpy as  np

def get_direction(img):
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grey, 80, 255, cv2.THRESH_BINARY_INV)

    edges = cv2.Canny(thresh, 200, 100)
#    return edges
    minLineLength = 1000
    maxLineGap = 0
    lines = cv2.HoughLinesP(edges, 1, np.pi/180.0, 50,
                        minLineLength, maxLineGap)
    if lines is not None:
        for line in lines:
            for x1, y1, x2, y2 in line:
                cv2.line(img, (x1, y1), (x2, y2), (0,255,0),2)
    
    return img
