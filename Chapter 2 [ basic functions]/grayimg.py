import cv2

img = cv2.imread("baby.jpg")
# i'm gonnna create grayscale

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray image", imgGray)
cv2.waitKey(0)