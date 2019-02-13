height_mm     = 70.94
width_mm      = 128.49
height_pixels = 1440
width_pixels  = 2560

height_mm     = 165.24
width_mm      = 293.76
height_pixels = 2160
width_pixels  = 3840

height_pitch = height_mm/height_pixels
width_pitch = width_mm/width_pixels
pitch = width_pitch

print("mm     ",height_mm,width_mm)
print("inch   ",height_mm/25.4,width_mm/25.4)
print("pixels ",height_pixels,width_pixels)
print("pitch  ",height_pitch,width_pitch)

