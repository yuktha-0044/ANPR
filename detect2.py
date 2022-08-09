import cv2
import pytesseract
import imutils
import fileselect as ft


pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR/tesseract.exe"
image = cv2.imread("image/car8.jpg")
image = imutils.resize(image, width=500)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.bilateralFilter(gray, 11, 17, 17)
edge = cv2.Canny(gray, 170, 200)
cnts, new = cv2.findContours(edge.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
image1 = image.copy()

cv2.drawContours(image1, cnts, -1, (0, 255, 0), 3)
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
NumberPlateCount = None
image2 = image.copy()
cv2.drawContours(image2, cnts, -1, (0, 255, 0), 3)
count = 0
name = 1
for i in cnts:
    perimeter = cv2.arcLength(i, True)
    approx = cv2.approxPolyDP(i, 0.02 * perimeter, True)
    if len(approx) == 4:
        x, y, w, h = cv2.boundingRect(i)
        crp_img = image[y:y+h, x: x+w]
        cv2.imwrite(str(name) + '.png', crp_img)
        name += 1
        break
crpImg = '1.png'

text = pytesseract.image_to_string(crpImg,  config="--psm 6", lang='eng')
print("car number is : ", text)

cv2.imshow('original image', image)
cv2.waitKey(0)

cv2.imshow('grey image', gray)
cv2.waitKey(0)

# cv2.imshow('smooth image', gray)
# cv2.imshow('canny image', edge)
# cv2.imshow('canny after contours', image1)
# cv2.imshow('cropped image', image2)
cv2.drawContours(image, cnts, -1, (0, 255, 0), 3)
cv2.waitKey(0)


#cv2.imshow('Final image', image)
cv2.imshow('Cropped image', cv2.imread(crpImg))
cv2.waitKey(0)

cv2.waitKey(0)

