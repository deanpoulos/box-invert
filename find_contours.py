import cv2 
from threshold_labels import *

def paint_contours(img):
    contours = get_contours(img)
    cv2.drawContours(img, contours, -1, (0,255,0), -1)

def get_contours(img):

    res = img.copy()
    thresh = cv2.getTrackbarPos(T, 'image')

    imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, thresh, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    return contours