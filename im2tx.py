import cv2
import os
import matplotlib.pyplot as plt
import easyocr
import PIL
PIL.Image.ANTIALIAS = PIL.Image.LANCZOS

bus_image = "bus7.png"
reader = easyocr.Reader(['en'])

result = reader.readtext(bus_image)

top_left = tuple(result[0][0][0])
bottom_right = tuple(result[0][0][2])
text = result[0][1]
font = cv2.FONT_HERSHEY_SIMPLEX
font_size = 5

img = cv2.imread(bus_image)
img = cv2.rectangle(img,top_left,bottom_right,(0,255,0),3)
img = cv2.putText(img,text,top_left, font, font_size ,(255,0,0),2,cv2.LINE_AA)

plt.imshow(img)
plt.show()