import cv2

# 元画像
img_raw = cv2.imread('template.bmp')

## マスク画像
img_mask = cv2.imread('mask2.bmp', 0)

## 画像の合成
img_syn = cv2.bitwise_and(img_raw, img_raw, mask=img_mask)

cv2.imshow('masked', img_syn)
cv2.waitKey(0)