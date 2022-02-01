import matplotlib.pyplot as plt
import numpy as np

file_path = "C:/Alpha/Data/SignalHistory.csv"

def go1():
   t, x1, x2 = np.loadtxt("C:/Alpha/Data/SignalHistory.csv", delimiter=",", unpack=True)

   print("data.shape",x1.shape, x2.shape)

   plt.plot(t,x1)
   plt.plot(t,x2)

   plt.xlabel('time')
   plt.ylabel('x1')
   plt.title('SignalHistory')
   plt.legend()
   plt.show()
