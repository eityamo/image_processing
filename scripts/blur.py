import cv2
img = cv2.imread("src/buildings.jpg")
# 平滑化処理
img_blur = cv2.blur(img, (3,3))
cv2.imshow("img", img_blur)
cv2.imshow("src", img)

# ガウシャンブラー
img_ga = cv2.GaussianBlur(img, (9,9), 2)
cv2.imshow("img1", img_ga)

# メディアンフィルター(中央値)
img_me = cv2.medianBlur(img, 5)
cv2.imshow("img2", img_me)

# バイラテラルフィルター
img_bi = cv2.bilateralFilter(img, 20, 30, 30)
cv2.imshow("img3", img_bi)

cv2.waitKey(0)
cv2.destroyAllWindows()