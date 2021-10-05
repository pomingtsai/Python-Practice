import math
from decimal import Decimal
import sys

# 定義輸入範圍錯誤的判斷
def input_aperture():
    aperture = float(input("請輸入光圈值：(1~22)"))
    if aperture < 1 or aperture > 22:
        print("您輸入的光圈值不在F1到F22之間!")
        sys.exit()
    else:
        return aperture
def input_distance():
    distance = float(input("請輸入被攝物體距離(m)："))
    if distance <= 0:
        print("距離不能小於或等於零!")
        sys.exit()
    else:
        return distance
def input_ISO():
    ISO = int(input("請輸入感光度ISO(100-102400)："))
    if ISO < 100 or ISO > 102400:
        print("您所輸入的ISO值不在100到102400之間!")
        sys.exit()
    else:
        return ISO

aperture = input_aperture()
distance = input_distance()
ISO = input_ISO()
GN = (aperture * distance) / math.sqrt((ISO / 100))
print("閃光燈出力值為", round(Decimal(GN), 1))