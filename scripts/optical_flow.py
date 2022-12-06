# オプティカルフローとは特徴点を見つけて、追いかけていく画像処理
# 1. 特徴点を見つける 
# 2. 特徴点とその周りは同じ方向を向くとして、流れを出す
# 3. 1と2を繰り返す
import cv2
cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img", 1200, 800)
COUNT = 500
# 収束条件
criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 20, 0.03)
# パラメーター定義
# 何段階か荒い画像を用意して特徴点を探す
lk_params = dict(winSize=(10,10), maxLevel=4, criteria=criteria)
cap = cv2.VideoCapture("movie/Cosmos.mp4")
# 1コマだけ読み込む
ret, frame = cap.read()
# 前の画像をグレースケールに直す
frame_pre = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
while True:
  ret, frame = cap.read()
  if ret == False:
    break
  frame_now = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  feature_pre = cv2.goodFeaturesToTrack(frame_pre, COUNT, 0.001, 5)
  if feature_pre is None:
    continue
  feature_now, status, err = cv2.calcOpticalFlowPyrLK(frame_pre, frame_now, feature_pre, None, **lk_params)
  for i in range(COUNT):
    # 特徴点を結ぶ
    pre_x = int(feature_pre[i][0][0])
    pre_y = int(feature_pre[i][0][1])
    now_x = int(feature_now[i][0][0])
    now_y = int(feature_now[i][0][1])
    cv2.line(frame, (pre_x, pre_y), (now_x, now_y), (255,0,0), 3)
  cv2.imshow("img", frame)
  frame_pre = frame_now.copy()
  if cv2.waitKey(10) == 27:
    break
cv2.destroyAllWindows()
