import cv2
import matplotlib.pyplot as plt
img = cv2.imread("src/grapes.jpg", 0)
cv2.imshow("img", img)
# 閾値を指定して2値化
threshould = 100
ret, img_th = cv2.threshold(img, threshould, 255, cv2.THRESH_BINARY)
# ret => 100
cv2.imshow("img_th", img_th)
# 閾値が可変
ret2, img_o = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
# ヒストグラムで可視化
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
cv2.imshow("otsu", img_o)
# 相対的な2値化
img_ada = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 1)
cv2.imshow("ada", img_ada)
cv2.waitKey(0)
cv2.destroyAllWindows()