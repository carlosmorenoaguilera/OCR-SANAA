import cv2 
import json
import os
import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path


# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

images = convert_from_path('HORARIOS AGUA POTABLE NOVIEMBRE2021.pdf')
if not (os.path.isfile('filename.txt')):
    for i in range(len(images)):
        images[i].save('page'+ str(i) +'.jpg', 'JPEG')
        

def process_image(imgname, lang_code):
    img = cv2.imread(imgname)
    return pytesseract.image_to_string(img, lang=lang_code)        

def output_file(filename, data):
	file = open(filename, "w+")
	file.write(data)
	file.close()

data_eng = process_image("page0.jpg", "eng")      
output_file("testSanaaPage0.txt", data_eng)
# img = cv2.imread('page0.jpg')
# h, w, c = img.shape
# boxes = pytesseract.image_to_boxes(img) 
# for b in boxes.splitlines():
#     b = b.split(' ')
#     img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

# #cv2.imshow('img', img)
# #cv2.waitKey(0)

# d = pytesseract.image_to_data(img, output_type=Output.DICT)
# f = open("demofile3.txt", "w")
# json.dump(d, f)
# f.close()
# print(d.keys())

# n_boxes = len(d['text'])
# for i in range(n_boxes):
#     if int(d['conf'][i]) > 60:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# cv2.imshow('img', img)
# cv2.waitKey(0)