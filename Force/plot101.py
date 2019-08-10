import matplotlib.pyplot as plt
import numpy as np

print("hello")

file_path = "./myforcelog.csv"

def go1():
   t, x1, pwm, vstop = np.loadtxt(file_path, delimiter=",", unpack=True)
   #data = np.loadtxt(file_path, delimiter=",")

   print("data.shape",x1.shape)

   plt.plot(t,x1)

   plt.xlabel('time')
   plt.ylabel('x1')
   plt.title('SignalHistory')
   plt.legend()
   plt.show()
