# インペイントとは
# 例）落書きの入った画像の落書きを消す
import cv2
import numpy as np
img = cv2.imread("src/Bus.jpg")
img_mask = cv2.imread("src/Mask.jpg", 0)
cv2.imshow("Mask", img_mask)
cv2.imshow("img", img)

# マスク画像の作成
thresh = 1
ret, img_bin = cv2.threshold(img_mask, thresh, 255, cv2.THRESH_BINARY)
cv2.imshow("bin", img_bin)

# インペイント
img_dst = cv2.inpaint(img, img_bin, 3, cv2.INPAINT_NS)
cv2.imshow("inpaint", img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()