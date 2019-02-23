import numpy as np

   
def go1():
   g1 = np.matrix('1, 0; 0, 1')
   print("g1")
   print(g1)

   g2 = np.matrix('0, -1; 1, 0')
   print("g2")
   print(g2)
   
   g3 = np.matrix('0,  1; -1, 0')
   print("g3")
   print(g3)

   x0 = np.matmul(g2,g3)
   print("x0")
   print(x0)
   
   x1 = np.matrix('11, 12; 21, 22')
   print("x1")
   print(x1)

   x2 = np.matmul(g2,np.matmul(x1,g3))
   print("x2")
   print(x2)
