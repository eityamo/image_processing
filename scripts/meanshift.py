# Meanshift/CamShiftはピクセルの密度が最大の場所を追いかける
# 1. ある場所から探索窓あ出発する（出発場所はユーザーが指定）
# 2. 探索窓内の画素地の重心を計算する
# 3. 探索窓の中心を重心に移す
# 4. 2と3を繰り返す
import cv2
cap = cv2.VideoCapture("movie/Cruse.mp4")
ret, frame = cap.read()
# 幅・高さ・チャンネル数
h, w, ch = frame.shape
# 探索点の開始点
rct = (600, 500, 200, 200)
cv2.namedWindow("win", cv2.WINDOW_NORMAL)
cv2.resizeWindow("win", 1200, 800)
# 収束条件
cri = (cv2.TERM_CRITERIA_COUNT | cv2.TERM_CRITERIA_EPS, 10, 1)
while(True):
  threshold = 100
  ret, frame = cap.read()
  if ret == False:
    break
  img_g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  ret, img_bin = cv2.threshold(img_g, threshold, 255, cv2.THRESH_BINARY)
  ret, rct = cv2.meanShift(img_bin, rct, cri)
  x, y, w, h = rct
  frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
  cv2.imshow("win", frame)
  if cv2.waitKey(10) == 27:
    break
cv2.destroyAllWindows()
