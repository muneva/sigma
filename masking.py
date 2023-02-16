import cv2 
import numpy as np
 
from fpdf import FPDF


# Görev-1 

img = cv2.imread('OpenCV_Logo.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([75, 100, 100])
upper_blue = np.array([130, 255, 255]) 

mask = cv2.inRange(hsv, lower_blue, upper_blue)

cv2.imshow('Mask',mask)
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 24)
pdf.cell(200, 10, txt = "1 - What is masking and how to create it?",
         ln = 1, align = 'C')

pdf.set_font("Arial", size = 14)
pdf.cell(200, 10, txt = "Masking is a type of filtering operation that filtres the spesific color of choice.",
         ln = 2, align = 'L')
pdf.cell(200, 10, txt = "For applying mask first we must convert bgr to hsv color scale than choose a color.",
         ln = 3, align = 'L')
pdf.cell(200, 10, txt = "In this example I masked the color blue in the inserted image.",
         ln = 4, align = 'L')
 

# Görev-2

cam = cv2.VideoCapture(0)

while(True):
    result, camImage = cam.read()
    cv2.imshow("Camera", camImage)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cam.release()
cv2.destroyAllWindows 


pdf.set_font("Arial", size = 24)
pdf.cell(200, 10, txt = "2 - How to capture a photo with camera?",
         ln = 8, align = 'C')

pdf.set_font("Arial", size = 14)
pdf.cell(200, 10, txt = "For opening the camera and capturing photo there is an OpenCV function.",
         ln = 9, align = 'L')
pdf.cell(200, 10, txt = "Which are cv2.VideoCapture and .read functions. Then we process the usual coding.",
         ln = 10, align = 'L')

pdf.output("23.02.02-Neva-Armagan.pdf")


# Görev-3

cam2 = cv2.VideoCapture(0)

while(True):
    result, camImage2 = cam2.read()

    hsv = cv2.cvtColor(camImage2, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([75, 100, 100])
    upper_blue = np.array([130, 255, 255]) 

    mask2 = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('Masked cam', mask2)

    if cv2.waitKey(1) & 0xFF == ord('x'):
        break

cam.release()
cv2.destroyAllWindows()