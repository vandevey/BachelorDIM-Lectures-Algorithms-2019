# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 14:01:56 2019

@author: vandevey
"""

import cv2 
import numpy as np 
img_gray = cv2.imread('image.png',0)
img = cv2.imread('image.png',1)

#display the matrix shapes
print("Gray levels image shape = "+str(img_gray.shape))
#print("BGR image shape = "+str(img_bgr.shape))

#display the loaded images
#cv2.imshow("Gray levels image", img_gray)
#cv2.imshow("image", img)
#cv2.waitKey()

# --- Invert Color

'''
def invert_color() :
    for row in range(img.shape[0]) :
        for col in range(img.shape[1]):
            for depth in range(img.shape[2]) :
                img[row, col, depth] = 255- img[row, col, depth]
    cv2.imshow("image inversé", img)
    cv2.waitKey()
invert_color()
'''

img = 255 - img