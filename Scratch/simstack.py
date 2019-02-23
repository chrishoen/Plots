from math import *
 
 
center_row = 2160/2
center_col = 3840/2
 
r = 2
b = 10

bottom_row1 = center_row - r
bottom_col1 = center_col - r
bottom_row2 = center_row - r
bottom_col2 = center_col + r
bottom_row3 = center_row + r
bottom_col3 = center_col + r
bottom_row4 = center_row + r
bottom_col4 = center_col - r

print("center")
print("%5d %5d" % (center_row, center_col))

print("bottom")
print("%5d %5d" % (bottom_row1,bottom_col1))
print("%5d %5d" % (bottom_row2,bottom_col2))
print("%5d %5d" % (bottom_row3,bottom_col3))
print("%5d %5d" % (bottom_row4,bottom_col4))
   
