import cv2
img = cv2.imread("src/floor.jpg", 0)
cv2.imshow("img", img)

# トラックバーが動いた時に動かす関数
def onTrackbar(position):
  global threshould
  threshould = position
# トラックバーを置くウィンドウ
cv2.namedWindow("img")
threshould = 100
cv2.createTrackbar("track", "img", threshould, 255, onTrackbar)
while True:
  # ret, img_th = cv2.threshold(img, threshould, 255, cv2.THRESH_BINARY)
  img_th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, threshould)
  cv2.imshow("img", img_th)
  cv2.imshow("src", img)
  if cv2.waitKey(10) == 27:
    break
cv2.destroyAllWindows()