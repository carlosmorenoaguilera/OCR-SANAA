from fpdf import FPDF
from os import listdir
from PIL import Image as PImage
pdf = FPDF()

# imagelist is the list with all image filenames


def loadImages(path):
    # return array of images

    imagesList = listdir(path)
    loadedImages = []
    for image in imagesList:
        img = PImage.open(path + image)
        loadedImages.append(img)

    return loadedImages


imagelist =  loadImages(r"C:/Users/Carlos Moreno/Pictures/Scans/declaracion")

for image in imagelist:
    pdf.add_page()
    pdf.image(image,x,y,w,h)
pdf.output("yourfile.pdf", "F")