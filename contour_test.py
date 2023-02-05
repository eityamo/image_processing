import cv2
import numpy as np

# ①「milkdrop.bmp」を読み込み、cv2.imshow()を用いて表示
img_raw = cv2.imread('template.bmp', 0)
# cv2.imshow('ImgRaw', img_raw)
# cv2.waitKey(0)
# height, width = img_raw.shape[:2]
# print("width: " + str(width))
# print("height: " + str(height))

img = cv2.resize(img_raw, dsize=None, fx=0.5, fy=0.5)

threshold = 55

ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

cv2.imshow("Image", img_thresh)
cv2.waitKey(0)

# cv2.CHAIN_APPROX_SIMPLE ココを変更して領域を指定
contours, hierarchy = cv2.findContours(img_thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# ノイズ除去
contours = list(filter(lambda x: cv2.contourArea(x) > 200, contours))

# for i, cnt in enumerate(contours):
#     print(f"contours[{i}].shape: {cnt.shape}")

threshold = 100

ret, img_thresh = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)

img_mask = np.zeros_like(img_thresh)

# cv2.drawContours(img_disp, contours, -1, (0, 0, 255), 2)
mask_outside = cv2.drawContours(img_mask, [contours[17]], -1, color=255, thickness=-1)
mask_inside = cv2.drawContours(img_mask, [contours[15]], -1, color=0, thickness=-1)
mask = mask_outside - mask_inside

# print([contours0])
# cv2.drawContours(img_disp, contours[8], -1, (0, 0, 255), 2)

# img_and = cv2.drawContours(img_mask, contours1, -1, color=255, thickness=-1)

# cv2.imshow("Image", img_mask)
# cv2.waitKey(0)

cv2.imshow("Image", img_mask)
cv2.waitKey(0)

# ②白色領域(ミルククラウン)とそれ以外の2値画像を作成
## 画像の読み込み
# img_binary = cv2.imread('OK.bmp', 0)
## 閾値の設定
# threshold = 137
## 2値化（閾値137を超えた画素を255にする。）
# img_thresh = cv2.threshold(img_binary, threshold, 255, cv2.THRESH_BINARY)[1]

# ③作成した2値画像をもとに、白色領域（ミルククラウン）の輪郭を抽出。画像リダリハ氏白色領域や細かい白いノイズがある場合は、大きさ判定や座標による抽出範囲の条件を加えてください。
## 白色の輪郭の外側の座標をcountoursに格納
# contours = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
## 面積が最大の輪郭を取得
# contour = max(contours, key=lambda x: cv2.contourArea(x))
## 輪郭の描画
# draw = cv2.drawContours(img_raw, contours, -1, color=(255, 255, 255), thickness=2)

# ④抽出した領域を用いて、ミルククラウン領域とそれ以外を分けたmask画像を作成
## マスク画像の作成
# img_mask = np.zeros_like(img_thresh)
# img_and = cv2.drawContours(img_mask, [contour], -1, color=255, thickness=-1)
# cv2.imshow('ImgAnd', img_and)
# cv2.waitKey(0)

# ⑤ミルククラウン領域のみを、cv2.imshow()を用いて表示
## 画像の合成
# img_syn = cv2.bitwise_and(img_raw, img_raw, mask=img_mask)

# cv2.imshow('masked_milkdrop', img_syn)
# cv2.waitKey(0)