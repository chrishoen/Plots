import matplotlib.pyplot as plt
import numpy as np

print("hello")

file_path = "./strain.csv"

def go1():
   t, x1 = np.loadtxt(file_path, delimiter=",", unpack=True)

   print("data.shape",x1.shape)

   ax1 = plt.subplot(111)
   plt.title('SignalHistory')
   plt.plot(t,x1)
   plt.ylabel('Force')
   ax1.set_ylim([-3,1])
   
   plt.show()

def go4():
   mTime, mY, mSignalXX, mDeviation, mDeviationLowXX, mDeviationLowFlag, mEvent = np.loadtxt(file_path, delimiter=",", unpack=True)

   #print("data.shape",x1.shape)

   #fig, (ax1,ax2,ax3) = plt.subplots(3,1,sharex='col')
   
   ax1 = plt.subplot(411)
   plt.title('SignalHistory')
   plt.plot(mTime,mY)
   plt.ylabel('Y')
   ax1.set_ylim([-5,5])

   ax2 = plt.subplot(412,sharex = ax1)
   plt.plot(mTime,mDeviation)
   plt.ylabel('Dev')
   ax2.set_ylim([-1,10])

   ax3 = plt.subplot(413,sharex = ax1)
   plt.plot(mTime,mDeviationLowXX)
   plt.xlabel('time')
   plt.ylabel('DevLowXX')
   ax3.set_ylim([-1,2])

   ax4 = plt.subplot(414,sharex = ax1)
   plt.plot(mTime,mDeviationLowFlag)
   plt.xlabel('time')
   plt.ylabel('DevLowFlag')
   ax4.set_ylim([-1,2])

   plt.show()
