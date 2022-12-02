# 畳み込みの流れ
# 1. フィルターを用意する
# 2. 着目がその周囲で（画素数）✖️（フィルター）を行い足していく＝畳み込み
# 3. 全ての画素について畳み込みを行う

import cv2
import numpy as np
# フィルターを作成
kernel = np.ones((3,3)) / 9.0
img = cv2.imread("src/Lena.jpg", 0)
# 畳み込みの操作
img_ke1 = cv2.filter2D(img, -1, kernel)
cv2.imshow("img", img_ke1)
cv2.imshow("src", img)

kernel2 = np.zeros((3,3))
kernel2[0,0] = 1
kernel2[1,0] = 2
kernel2[2,0] = 1
kernel2[0,2] = -1
kernel2[1,2] = -2
kernel2[2,2] = -1

img_ke2 = cv2.filter2D(img, -1, kernel2)
cv2.imshow("src2", img_ke2)
cv2.waitKey(0)
cv2.destroyAllWindows()