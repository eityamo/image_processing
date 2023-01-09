import cv2
# Mac
# HAAR_FILE = "/Users/eityamo/opt/anaconda3/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml"
# Windows
HAAR_FILE = "C:\\Users\\proscons\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)
img = cv2.imread("src/Solvay_conference_1927.jpg")
img_g = cv2.imread("src/Solvay_conference_1927.jpg", 0)

# 画像が存在する場所を格納
face = cascade.detectMultiScale(img_g)
for x, y, w, h in face:
  cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()