# 計算找錢
# 新台幣面額種類

product_price = int(input("請輸入商品價格: "))
money_paid = int(input("請輸入要拿多少錢付款: "))

if money_paid < product_price:
    print("您拿出的錢不夠支付商品價格!")
else:
    print("共找回",money_paid - product_price,"元.")
