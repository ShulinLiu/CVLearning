import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

def traslate(image,x,y):
	M = np.float32([[1,0,x],[0,1,y]])
	shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
	return shifted


image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# matrix for translation
# coordinate
# ----------------->x
#   |
#   |
#   |
#   |
M = np.float32([[1,0,25], [0,1,50]])
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("shifted Down and Right",shifted)

# matrix for translation
M = np.float32([[1,0,-50], [0,1,-90]])
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("shifted Up and Left",shifted)
cv2.waitKey(0)
