import img2pdf
from PIL import Image
import os

img_path = str(input("Enter the file path with file name, including its extension: "))
pdf_path = str(input("Enter file of the path to be created: "))
pdf_name = str(input("Enter the pdf file name: "))
pdf_path_name = pdf_path + pdf_name

image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path_name, "wb")
file.write(pdf_bytes)

image.close()
file.close()

print("Successfully made pdf file!")