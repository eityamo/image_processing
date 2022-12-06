import cv2
import numpy as np
cap = cv2.VideoCapture("movie/Mobility.mp4")
while True:
  cv2.namedWindow("img", cv2.WINDOW_NORMAL)
  cv2.resizeWindow("img", 640, 480)
  # 1フレームだけ読み込み
  ret, frame = cap.read()
  if ret == False:
    break
  # HSV空間に変換
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  # 黄色の定義(Hは実際は40ぐらい)
  lower = np.array([20, 50, 50])
  upper = np.array([25, 255, 255])
  # 黄色だけが保存
  frame_mask = cv2.inRange(hsv, lower, upper)
  # 2値画像の論理積をとる
  dst = cv2.bitwise_and(frame, frame, mask = frame_mask)
  cv2.imshow('img', dst)
  if cv2.waitKey(10) == 27:
    break
cv2.destroyAllWindows()