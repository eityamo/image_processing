import cv2
import numpy as np
img = cv2.imread("src/road.jpg")
img_g = cv2.imread("src/road.jpg", 0)
cv2.imshow("img", img)
img_canny = cv2.Canny(img_g, 300, 450)
cv2.imshow("canny", img_canny)

# 直線を検出
lines = cv2.HoughLines(img_canny, 1, np.pi/180, 100)

# 直線の描写
for i in lines[:]:
  rho = i[0][0]
  theta = i[0][1]
  a = np.cos(theta)
  b = np.sin(theta)
  xθ = rho * a
  yθ = rho * b
  x1 =int(xθ + 1000 * (-b))
  y1 =int(yθ + 1000 * (a))
  x2 =int(xθ - 1000 * (-b))
  y2 =int(yθ - 1000 * (a))
  cv2.line(img, (x1, y1), (x2, y2), (255, 0, 0), 1)

cv2.imshow("line", img)

cv2.waitKey(0)
cv2.destroyAllWindows()