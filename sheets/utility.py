import sys
import os
from wand.image import Image
from pdfrw import PdfReader

PDF_EXT    = '.pdf'
IMAGE_EXT  = '.jpg'
RESOLUTION = 500

def convert_pdf_to_image(pdf_file, dest_dir):
    filename, ext = os.path.splitext(pdf_file)
    if os.path.exists(pdf_file) and ext == PDF_EXT:
        pages = PdfReader(pdf_file, decompress=False).pages
        for i in range(len(pages)):
            with Image(filename=pdf_file + '[' + str(i) + ']', resolution=RESOLUTION) as img:
                img.save(filename=os.path.join(dest_dir, str(i) + IMAGE_EXT))

def count_images_in_dir(dir):
    if (os.path.exists(dir)):
        return len([f for f in os.listdir(dir)
                    if os.path.isfile(os.path.join(dir, f))
                    and f.endswith(IMAGE_EXT)])
