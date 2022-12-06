import cv2
import numpy as np
img = cv2.imread("src/drive.jpg")
h, w = img.shape[:2]
cv2.imshow("img", img)
# 基準の点
per1 = np.float32([[100, 500], [300, 500], [300, 100], [100, 100]])
# 対応後の点
per2 = np.float32([[100, 500], [300, 500], [280, 200], [150, 200]])
# 変換の行列
psp_matrix = cv2.getPerspectiveTransform(per1, per2)
img_psp = cv2.warpPerspective(img, psp_matrix, (w,h))
cv2.imshow("psp", img_psp) 
cv2.waitKey(0)
cv2.destroyAllWindows()