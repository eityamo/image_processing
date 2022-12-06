import cv2
import matplotlib.pyplot as plt

img = cv2.imread("src/Lena.jpg", 0)
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
img_eq = cv2.equalizeHist(img)
hist_e = cv2.calcHist([img_eq], [0], None, [256], [0,256])
plt.plot(hist_e)
plt.show()
cv2.imshow("img", img)
cv2.imshow("eq", img_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()
