import cv2
import sys

cap = cv2.VideoCapture("movie/Cosmos.mp4")
# 正しく動画を読み込めたかを確認
if cap.isOpened() == False:
  # プログラムから抜ける
  sys.exit()
# 1フレームだけ動画を読み込む
ret, frame = cap.read()
# frameのshapeを取得
h, w = frame.shape[:2]
# 書き込みの設定
fourcc = cv2.VideoWriter_fourcc(*"XVID")
dst = cv2.VideoWriter("output/test.avi", fourcc, 30.0, (w,h))

while True:
  ret, frame = cap.read()
  if ret == False:
    break
  cv2.imshow("img", frame)
  dst.write(frame)
  # 動画の再生中のESCキーが押されると動画が終了
  if cv2.waitKey(30) == 27:
    break
cv2.destroyAllWindows()
cap.release()