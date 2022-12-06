import cv2
import numpy as np

img = cv2.imread("src/grapes.jpg")
img_g = cv2.imread("src/grapes.jpg", 0)
cv2.imshow("img", img)

# 円を検出する対象
circles = cv2.HoughCircles(img_g, cv2.HOUGH_GRADIENT, dp=1, minDist=1, param1=20, param2=35, minRadius=1, maxRadius=30)

# 円の描写
for i in circles[0]:
  x = int(i[0])
  y = int(i[1])
  r = int(i[2])
  cv2.circle(img, (x,y), r, (255, 0, 0), 1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()