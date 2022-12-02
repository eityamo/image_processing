# アファイン変換とは回転や平行移動などの線形変換
import cv2
import numpy as np
img = cv2.imread("src/grapes.jpg")
h, w = img.shape[:2]
# 画像を30pxずつ平行移動
dx, dy = 30, 30
# 変換行列を定義
afn_mat = np.float32([[1,0,dx],[0,1,dy]])
# アファイン変換を画像に反映
img_afn = cv2.warpAffine(img, afn_mat, (w,h))
cv2.imshow("trans", img_afn)
cv2.waitKey(0)
cv2.destroyAllWindows()