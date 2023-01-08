import cv2
# ヒストグラムを使うから
import matplotlib.pyplot as plt
# %matplotlib inline
img = cv2.imread("src/Lena.jpg")

# ヒストグラムのリスト
color_list = ["blue", "green", "red"]
for i,j in enumerate(color_list):
  hist = cv2.calcHist([img], [i], None, [256], [0,256])
  plt.plot(hist, color = j)

img_gray = cv2.imread("src/Lena.jpg", 0)
hist2 = cv2.calcHist([img_gray], [0], None, [256], [0,256])
plt.plot(hist2)

plt.show()
