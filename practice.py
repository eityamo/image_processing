import cv2
import numpy as np

# ①「milkdrop.bmp」を読み込み、cv2.imshow()を用いて表示
img_origin = cv2.imread('milkdrop.bmp')
cv2.imshow('ImageOrigin', img_origin)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ②白色領域(ミルククラウン)とそれ以外の2値画像を作成
## 画像の読み込み
img_binary = cv2.imread('milkdrop.bmp', 0)
## 閾値の設定
threshold = 137
## 2値化（閾値137を超えた画素を255にする。）
img_thresh = cv2.threshold(img_binary, threshold, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('ImageOrigin', img_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()