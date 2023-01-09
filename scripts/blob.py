import cv2
import copy
img = cv2.imread("src/Blob.png")
img_g = cv2.imread("src/Blob.png", 0)

ret, img_bi = cv2.threshold(img_g, 100, 255, cv2.THRESH_BINARY)
nLabels, labelImage, stats, centroids = cv2.connectedComponentsWithStats(img_bi)

# nlabel 検出したブロブの個数（背景含む）
# labelImage ラベルのIDが降られている配列
# stats [最小のX, 最小のY, 幅, 高さ, ブロブの面積]
# cantroids 重心の座標

# imgのコピー
img_blob = copy.deepcopy(img)
h, w = img_g.shape
# 代入する色のリスト
color = [[255,0,0], [0,255,0], [0,0,255], [255,255,0]]

# 図形の色塗り
for y in range(h):
  for x in range(w):
    if labelImage[y,x] > 0:
      img_blob[y,x] = color[labelImage[y,x]-1]

# 図形の重心に書き込む
for i in range(1, nLabels):
  xc = int(centroids[i][0])
  yc = int(centroids[i][1])
  font = cv2.FONT_HERSHEY_COMPLEX
  scale = 1
  color = (255,255,255)
  cv2.putText(img_blob, str(stats[i][-1]), (xc, yc), font, scale, color)

cv2.imshow("bi", img_bi)
cv2.imshow("img2", img_blob)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()