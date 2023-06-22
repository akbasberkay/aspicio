import numpy as np 

import matplotlib.pyplot as plt
#%matplotlib inline

from PIL import Image

pic = Image.open('C:/Users/Berkay Akbaş/Downloads/Computer-Vision-with-Python/Computer-Vision-with-Python/DATA/00-puppy.jpg')

pic_arr = np.asarray(pic)

print(pic_arr.shape)

#filter the red one only

pic_arr_red = pic_arr.copy()

pic_arr_red[:,:,1] = 0
pic_arr_red[:,:,2] = 0

plt.imshow(pic_arr_red)

plt.show()
