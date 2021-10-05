# 金額折扣計算
# 滿10萬打八折，滿5萬打八五折，滿3萬打九折，滿1萬打九五折

from decimal import Decimal
import math

discount = int(input("請輸入購買金額："))
if discount >= 10000:
    if discount >= 100000:
        print("您所購買的金額打八折後為", round(Decimal(discount * 0.8), 0), "元 \n")
    elif discount >= 50000:
        print("您所購買的金額打八五折後為", round(Decimal(discount * 0.85), 0), "元 \n")
    elif discount >= 30000:
        print("您所購買的金額打九折後為", round(Decimal(discount * 0.9), 0), "元 \n")
    elif discount >= 10000:
        print("您所購買的金額打九五折後為", round(Decimal(discount * 0.95), 0), "元 \n")
else:
    print("您所購買的金額沒有達到折扣標準 \n")