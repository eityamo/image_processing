import cv2
img = cv2.imread("src/grapes.jpg")
# グレースケールに変換
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# hsvへの変換
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(img_gray.shape)
# => (640, 960)
print(img_hsv.shape)
# => (640, 960, 3)

# グレースケール化の簡単な方法
img_gray2 = cv2.imread("src/grapes.jpg", 0)
cv2.imshow("gray", img_gray2)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img_hsv)
