# アファイン変換とは回転や平行移動などの線形変換
import cv2
import numpy as np
img = cv2.imread("src/grapes.jpg")
h, w = img.shape[:2]
# 画像を30pxずつ平行移動
dx, dy = 30, 30
# 変換行列を定義 中心を軸に反時計回りに40°回転
rot_mat = cv2.getRotationMatrix2D((w/2, h/2), 40, 1)
# アファイン変換を画像に反映
img_afn = cv2.warpAffine(img, rot_mat, (w,h))
cv2.imshow("rotation", img_afn)
cv2.waitKey(0)
cv2.destroyAllWindows()