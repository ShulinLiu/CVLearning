from __future__ import print_function
import matplotlib
matplotlib.use('TkAgg')
import argparse
import numpy as np
import matplotlib.pyplot as plt
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
# image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

# hist = cv2.calcHist([image],[0],None,[256],[0,256])
chans = cv2.split(image)
colors = ("b","g","r")

plt.figure()
plt.title("Flatterned Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
# plt.plot(hist)
# plt.xlim([0,256])
# plt.show()
# cv2.waitKey(0)
for (chan,color) in zip(chans,colors):
	hist = cv2.calcHist([chan],[0],None,[256],[0,256])
	plt.plot(hist,color=color)
	plt.xlim([0,256])