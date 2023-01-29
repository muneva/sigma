import cv2
import numpy as np

#200x300 siyah resim 
image = np.zeros((200,300,3), dtype = "uint8")
cv2.imshow("black", image)

#dosyadan çağırdığım resim üzerine daire, çizgi, kare ve yazı eklemek
img = cv2.imread("OpenCV_Logo.png", 0)
img = cv2.resize(img, (300, 200))

cv2.line(img, (150,100), (300,200), (0,0,255), 2)
cv2.line(img, (150,100), (0,200), (0,0,255), 2)
cv2.rectangle(img, (100,50), (200,150), (0,0,255), 2)
cv2.circle(img, (150,100), 50, (0,0,255), 2)
cv2.putText(img, "vatican cameos", (25,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0))

cv2.imshow("image2", img)

cv2.waitKey(0)
cv2.destroyAllWindows()