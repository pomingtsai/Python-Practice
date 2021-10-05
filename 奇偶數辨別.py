# 奇偶數辨別 (Odd or even)
num = int(input("請輸入一個介於1到1000之間的整數："))
if num < 1 or num > 1000:
    print("您所輸入的數字不是介於1到1000之間！")
else:
    if num % 2 == 0:
        print("您所輸入的數字",num,"是一個偶數值。")
    else:
        print("您所輸入的數字",num,"是一個奇數值。")
    