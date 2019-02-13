import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D


input_file_path = "C:/Alpha/Image/InputImage.png"
output_file_path = "C:/Alpha/Image/OutputImage.png"
input_image = mpimg.imread(input_file_path)
output_image = mpimg.imread(output_file_path)

crow = 200
ccol = 200
arow = 150
acol = 150
brow = 250
bcol = 250
n = 3
m = n*2 + 1

input_roi  = input_image[brow-n:brow+n+1,bcol-n:bcol+n+1]
output_roi = output_image[brow-n:brow+n+1,bcol-n:bcol+n+1]

np.set_printoptions(precision=5,linewidth=100,suppress=True)
np.set_printoptions(formatter={'float': '{: 0.3f}'.format})


def go1():
   print(output_image.shape)
   plt.imshow(output_image)
   plt.show()
   
   
def go2():
   print("input_image.shape ", input_image.shape)
   print("output_image.shape", output_image.shape)
   print("input_roi.shape   ", input_roi.shape)
   print("output_roi.shape  ", output_roi.shape)
