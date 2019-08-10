import matplotlib.pyplot as plt
import numpy as np

print("hello")

file_path = "./myforcelog.csv"

def go1():
   t, x1, pwm, vstop = np.loadtxt(file_path, delimiter=",", unpack=True)

   print("data.shape",x1.shape)

   plt.plot(t,x1)

   plt.xlabel('time')
   plt.ylabel('x1')
   plt.title('SignalHistory')
   plt.show()

def go3():
   t, x1, pwm, vstop = np.loadtxt(file_path, delimiter=",", unpack=True)

   print("data.shape",x1.shape)

   ax1 = plt.subplot(3,1,1)
   plt.title('SignalHistory')
   plt.plot(t,x1)
   plt.ylabel('Force')
   ax1.set_ylim([-5,5])

   ax2 = plt.subplot(3,1,2)
   plt.plot(t,pwm)
   plt.ylabel('PWM')
   ax2.set_ylim([-200,1000])

   ax3 = plt.subplot(3,1,3)
   plt.plot(t,vstop)
   plt.xlabel('time')
   plt.ylabel('VSTOP')
   ax3.set_ylim([-1,2])

   plt.show()
