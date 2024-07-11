# test file if you want to quickly try tesseract on a license plate image
#https://digi.bib.uni-mannheim.de/tesseract/

import pytesseract
import cv2
import os
import numpy as np
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

engine = pyttsx3.init()

gray = cv2.imread("bus7.png" )
gray = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
gray = cv2.resize(gray, (640, 480))
gray = cv2.bitwise_not(gray)
bus_name = ""
# Extract text from the image

text = pytesseract.image_to_string(gray, config='-c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 3 --oem 3')
print(text)
bus_name += text
print(bus_name)


engine.say(bus_name)
engine.save_to_file(bus_name, 'test.mp3')
engine.runAndWait()


cv2.waitKey(0)
cv2.destroyAllWindows()