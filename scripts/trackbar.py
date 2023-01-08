import cv2
def onTrackbar(position):
  global trackValue
  trackValue = position

# トラックバー初期値
trackValue = 100
# ウィンドウを作成
cv2.namedWindow("img")
# トラックバーを作成
cv2.createTrackbar("track", "img", trackValue, 255, onTrackbar)
cv2.waitKey(0)
cv2.destroyAllWindows()