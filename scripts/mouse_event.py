import numpy as np
import cv2

# ダブルクリックすると座標を表示
def print_position(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDBLCLK:
    print(x,y)
# 画像作成
img = np.zeros((512,512), np.uint8)
cv2.namedWindow("img")
# imgの中で命令があった場合にprint_positionを実行する
cv2.setMouseCallback("img", print_position)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
