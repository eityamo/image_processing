import cv2
img = cv2.imread("src/Blob.png")
img_g = cv2.imread("src/Blob.png", 0)
ret, img_bi = cv2.threshold(img_g, 100, 255, cv2.THRESH_BINARY)
# 輪郭の抽出
contours, hierarchy = cv2.findContours(img_bi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 取得した輪郭を描写
img_contour = cv2.drawContours(img, contours, -1, (255, 0, 0), 1)
cv2.imshow("img", img_contour)
cv2.waitKey(0)
cv2.destroyAllWindows()
