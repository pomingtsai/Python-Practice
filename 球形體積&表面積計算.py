# 球形體積 4/3 * math.pi() * r^3
# 球形表面積 4 * math.pi() * r^2

import math

circle_radius = float(input("請輸入半徑(cm):"))
circle_volume = round((4 / 3) * math.pi * (circle_radius ** 3), 1)
circle_surface_area = round(4 * math.pi * (circle_radius ** 2), 1)
print("半徑",circle_radius,"cm，\n球形體積為",circle_volume,"立方公分，\n球形表面積為",circle_surface_area,"平方公分。")