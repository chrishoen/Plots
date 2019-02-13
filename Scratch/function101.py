import matplotlib.pyplot as plt
import numpy as np

def fn1(x):
   return x*x

sigma = 3

def fn2(x):
   return np.exp(-x*x/2*sigma*sigma)

def fn3(r):
   return np.exp(-r)/r

def fn4(r):
   return 1/r

def fn5(r):
   return 1/(r*r)

def go1():
   x = np.linspace(-5., 5., 1000)
   y = fn2(x)

   plt.plot(x,y)
   plt.xlabel('X')
   plt.ylabel('Y')
   plt.title('Function')
   plt.show()

def go2():
   x = np.linspace(1., 5., 1000)
   y = fn5(x)

   plt.plot(x,y)
   plt.xlabel('X')
   plt.ylabel('Y')
   plt.title('Function')
   plt.show()


go2()