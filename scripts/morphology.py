# モルフォロジー演算とは膨張と収縮からなる
# 幅せるを収縮させたり、膨張させると図形を分離・一体化できる
# オープニング・クロージングは図形の大きさを保ちながら形状操作ができる
import cv2
import numpy as np
img = cv2.imread("src/floor.jpg", 0)
ret, img_th = cv2.threshold(img, 110, 255, cv2.THRESH_BINARY)
cv2.imshow("img", img_th)

# 着目画素（3、3）を黒にするか白にするか
kernel = np.ones((3,3), dtype=np.uint8)
# dilate
img_d = cv2.dilate(img_th, kernel)
# erode
img_e = cv2.erode(img_th, kernel)

cv2.imshow("e", img_e)
cv2.imshow("d", img_d)

# クロージング
img_c = cv2.morphologyEx(img_th, cv2.MORPH_CLOSE, kernel)
cv2.imshow("c", img_c)

# オープニング
img_o = cv2.morphologyEx(img_th, cv2.MORPH_OPEN, kernel)
cv2.imshow("o", img_o)

cv2.waitKey(0)
cv2.destroyAllWindows()