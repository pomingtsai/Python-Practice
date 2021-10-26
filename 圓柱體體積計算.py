# 圓柱體體積計算
import math
cylinder_radius = float(input("請輸入圓柱體的半徑(cm)："))
cylinder_height = float(input("請輸入圓柱體的高度(cm)："))
cylinder = math.pi * (cylinder_radius ** 2) * cylinder_height
print("圓柱體體積為", round(cylinder, 2), "立方公分")
print("圓柱體容積為", round((cylinder / 1000), 2), "公升")