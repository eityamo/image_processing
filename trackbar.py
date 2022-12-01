import cv2
def onTrackbar(position):
  global trackValue
  trackValue = position

trackValue = 100
cv2.namedWindow("img")
cv2.createTrackbar("track", "img", trackValue, 255, onTrackbar)
cv2.waitKey(0)
cv2.destroyAllWindows()