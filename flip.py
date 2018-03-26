import cv2

image = cv2.imread('paofu.jpg',1)

flipped = cv2.flip(image,1)
cv2.imshow("Flipped horizontally", flipped)
cv2.waitKey(0)
cv2.destroyAllWindows()