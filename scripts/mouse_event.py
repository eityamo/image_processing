import numpy as np
import cv2
def print_position(event, x, y, flags, param):
  if event == cv2.EVENT_LBUTTONDOWN:
    print(x,y)
img = np.zeros((512,512), np.uint8)
cv2.namedWindow("img")
cv2.setMouseCallback("img", print_position)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
