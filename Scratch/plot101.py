import matplotlib.pyplot as plt
import numpy as np

file_path = "C:/Alpha/Data/temp.csv"
file_path = "C:/Alpha/Data/SignalHistory.csv"

def go1():
   t, x1 = np.loadtxt("C:/Alpha/Data/SignalHistory.csv", delimiter=",", unpack=True)
   #data = np.loadtxt(file_path, delimiter=",")

   print("data.shape",x1.shape)

   plt.plot(t,x1)

   plt.xlabel('time')
   plt.ylabel('x1')
   plt.title('SignalHistory')
   plt.legend()
   plt.show()
