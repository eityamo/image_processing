# openCVを作るため
import cv2
# 出力する先のフォルダを作るため
import os

# 画像の読み込み
img = cv2.imread("src/Berry.jpg")
# (高さ, 幅, 画素値数) = (589, 960, 3)
print(img.shape)
# numpyの配列を表示
print(img)
# 画像の表示
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 画像の出力
cv2.imwrite("output/test.jpg", img)
