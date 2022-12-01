import cv2
import numpy as np

# 500✖️500の白のキャンバスを作成
img = np.ones((500,500,3)) * 255

# 青い直線の描写
cv2.line(img, (0,0), (150,190), (255, 0, 0), 2)
# 緑色の四角形の描写
cv2.rectangle(img, (100,25), (300,150), (0, 255, 0), 4)
# 青い塗りつぶされた円の描写
cv2.circle(img, (100,100), 55, (0, 0, 255), -1)
# 楕円の描写
cv2.ellipse(img, (250, 250), (100, 50), 20, 0, 360, (255, 0, 0), 1)
# 折れ線の描写
pts = np.array([[100, 30], [200, 30], [200, 80], [100, 50]])
cv2.polylines(img, [pts], False, (100, 255, 0), 3)
# テキスト
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (100, 300), font, 1, (0,255,0), 3, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()