import matplotlib.pyplot as plt
import numpy as np

print("hello")

file_path = "./myforcelog.csv"

def go1():
   t, x1 = np.loadtxt(file_path, delimiter=",", unpack=True)

   print("data.shape",x1.shape)

   ax1 = plt.subplot(111)
   plt.title('SignalHistory')
   plt.plot(t,x1)
   plt.ylabel('Force')
   ax1.set_ylim([-3,1])
   
   plt.show()

def go3():
   t, x1, pwm, vstop = np.loadtxt(file_path, delimiter=",", unpack=True)

   print("data.shape",x1.shape)

   #fig, (ax1,ax2,ax3) = plt.subplots(3,1,sharex='col')
   
   ax1 = plt.subplot(311)
   plt.title('SignalHistory')
   plt.plot(t,x1)
   plt.ylabel('Force')
   ax1.set_ylim([-5,5])

   ax2 = plt.subplot(312,sharex = ax1)
   plt.plot(t,pwm)
   plt.ylabel('PWM')
   ax2.set_ylim([-200,1000])

   ax3 = plt.subplot(313,sharex = ax1)
   plt.plot(t,vstop)
   plt.xlabel('time')
   plt.ylabel('VSTOP')
   ax3.set_ylim([-1,2])

   plt.show()
