import cv2
import matplotlib.pyplot as plt
import numpy as np

## IMPORTING A COLORED IMAGE

img = cv2.imread('00-puppy.jpg')
    # HAS 3 DIMENSIONS
fixed_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(fixed_img)
plt.show()

## IMPORTING A GREYSCALE IMAGE

img_gray = cv2.imread('00-puppy.jpg', cv2.IMREAD_GRAYSCALE)
    # HAS ONLY 1 DIMENSION
plt.imshow(img_gray,cmap='gray')

plt.show()

## RESIZING AN IMAGE

squeezed_img = cv2.resize(fixed_img, (1000, 400)) # width first, height second

plt.imshow(squeezed_img)

plt.show()

w_ratio = 0.5
h_ratio = 0.5

half_size_img = cv2.resize(fixed_img, (0,0), fixed_img, w_ratio, h_ratio)

plt.imshow(half_size_img)

plt.show()

## FLIPPING AN IMAGE

flipped_img = cv2.flip(fixed_img,0)
    # 0 means x axis
    # 1 means y axis
    # -1 means both
plt.imshow(flipped_img)

plt.show()

## SAVE AN IMAGE

cv2.imwrite('half_sized.jpg', half_size_img)