# image_resizing.py

# imports
import cv2
import os
from os import listdir
import glob
from PIL import Image

# inputs
input_folder = r'public/data/input_ims'
output_folder = r'public/data/output_ims'

# # convert tifs to jpgs
# for im in os.listdir(input_folder):
#     # check if image is a tif
#     if (im.endswith(".tif")):
#         image = Image.open(f'{input_folder}/{im}')
#         im = im.removesuffix('.tif')
#         image.convert('CMYK').save(f'{input_folder}/{im}.jpg')

# TIFS END UP LOOKING WEIRD :( need to find a fix

# for each image in the folder
for img in glob.glob(input_folder + "/*.jpg"):
    image = cv2.imread(img)
    # resize image to 18% it's original size
    imgResized = cv2.resize(image, None, fx = 0.18, fy = 0.18)
    # save images to output folder with same name
    cv2.imwrite(os.path.join(output_folder, img.split(os.path.sep)[-1]), imgResized)