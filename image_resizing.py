# image_resizing.py

# imports
import cv2
import os
import glob

# inputs
input_folder = r'public/data/input_ims'
output_folder = r'public/data/output_ims'

# for each image in the folder
for img in glob.glob(input_folder + "/*.jpg"):
    # read image
    image = cv2.imread(img)
    # resize image to 18% it's original size
    imgResized = cv2.resize(image, None, fx = 0.18, fy = 0.18)
    # save images to output folder with same name
    cv2.imwrite(os.path.join(output_folder, img.split(os.path.sep)[-1]), imgResized)