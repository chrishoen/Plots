import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from mpl_toolkits.mplot3d import Axes3D


file_path = "C:/Alpha/Image/OutputImage.png"
image = mpimg.imread(file_path)

def go1():
   print(image.shape)
   plt.imshow(image)
   plt.show()
   
   
def go2():
   # create the x and y coordinate arrays (here we just use pixel indices)
   xx, yy = np.mgrid[0:image.shape[0], 0:image.shape[1]]

   # show
   print("image.shape", image.shape)
   print("xx.shape   ", xx.shape)
   print("yy.shape   ", yy.shape)

   # create the figure
   levels = np.arange(0.0, 255, 20)
   fig,ax = plt.subplots()
   ax.contour(xx,yy, image)

   # show
   plt.show()   
   
   
   