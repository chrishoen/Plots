from math import *
 
 
center_row = 2160/2
center_col = 3840/2
 
r = 500
a = 2*pi/24

rows = []
cols = [] 

for n in range(0,12):
   b = 2*pi*n/12 + a
   rows.append(center_row + r*sin(b))
   cols.append(center_col + r*cos(b))

   
print("floats")
for n in range(0,12):
   print("rc %10.2f %10.2f" % (rows[n],cols[n]))
   
print("ints")
for n in range(0,12):
   print("%5d %5d" % (round(rows[n]),round(cols[n])))
   
