# 特徴抽出
# 特徴とはパターン認識に役立つ情報量の多い部分のこと
import cv2
import numpy as np
import copy
img = cv2.imread("src/buildings.jpg")
img_g = cv2.imread("src/buildings.jpg", 0)
img_harris = copy.deepcopy(img)
# コーナー検出
img_dst = cv2.cornerHarris(img_g, 2, 3, 0.04)

# Harrisのコーナー検出
# 特徴点を書き込む
img_harris[img_dst > 0.05 * img_dst.max()] = [0, 0, 255]
cv2.imshow("Harris", img_harris)

# imgのコピー
img_kaze = copy.deepcopy(img)
# 特徴抽出キーをKAZEの中に入れる
kaze = cv2.KAZE_create()
# 特徴点の情報を入れる
kp1 = kaze.detect(img, None)

img_kaze = cv2.drawKeypoints(img_kaze, kp1, None)
cv2.imshow("AKAZE", img_kaze)

img_orb = copy.deepcopy(img)
orb = cv2.ORB_create()
kp2 = orb.detect(img_orb)
img_orb = cv2.drawKeypoints(img_orb, kp2, None)
cv2.imshow("ORB", img_orb)

cv2.waitKey(0)
cv2.destroyAllWindows()

