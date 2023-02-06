import cv2
import numpy as np

def imshow(img):
    cv2.imshow('gamma', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def adjust(img, alpha=1.0, beta=0.0):
    # 積和演算を行う。
    dst = alpha * img + beta
    # [0, 255] でクリップし、uint8 型にする。
    return np.clip(dst, 0, 255).astype(np.uint8)

alpha1 = [1.2, 1.4]
beta1 = [-25, 25, 50]

for i in alpha1:
    for j in beta1:
        # 画像を読み込む。
        src = cv2.imread("data/NG (3).jpg")

        # コントラスト、明るさを変更する。
        dst = adjust(src, alpha=i, beta=j)
        
        cv2.imwrite(f'data/result{j}{i}.jpg', dst)

