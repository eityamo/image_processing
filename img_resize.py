import cv2
img = cv2.imread("src/grapes.jpg")
# cv2.imshow("img", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
print(img.shape)
# =>(640, 960, 3)
size = (300, 200)
# 画像のリサイズ
img_resize = cv2.resize(img, size)
print(img_resize.shape)
# # =>(200, 300, 3)
# cv2.imshow("resize", img_resize)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# リサイズのやり方の比較
img_area = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
img_linear = cv2.resize(img, size, interpolation = cv2.INTER_LINEAR)
# 自然な仕上がり
cv2.imshow("area", img_area)
# チカチカした仕上がり
cv2.imshow("linear", img_linear)
cv2.waitKey(0)
cv2.destroyAllWindows()