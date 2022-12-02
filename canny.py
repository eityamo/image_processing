# Cannyのアルゴリズム
# 1. ガウシアンフィルタでぼかす（ノイズを取り除く）
# 2. Sobelふぃるたーで微分する（x方向、y方向に微分する）
# 3. 極大点を探す
# 4. 2段階の閾値処理によってエッジを残す

import cv2
img = cv2.imread("src/Lena.jpg", 0)
# Cannyのエッジ検出機を使う（2つの閾値を設定）
img_canny = cv2.Canny(img, 100, 200)
cv2.imshow("Canny", img_canny)
cv2.waitKey(0)
cv2.destroyAllWindows()