import sys
import os
from wand.image import Image
from pdfrw import PdfReader

def convert_pdf_to_jpg(pdf_file, dest_dir):
    filename, ext = os.path.splitext(pdf_file)
    if os.path.exists(pdf_file) and ext == '.pdf':
        pages = PdfReader(pdf_file, decompress=False).pages
        for i in range(len(pages)):
            with Image(filename=pdf_file + '[' + str(i) + ']', resolution=500) as img:
                img.save(filename=dest_dir + str(i) + '.jpg')
