# 請使用者輸入一個整數，以獲得其因數

numbers = int(input("請輸入一個整數："))
div_set = []
for i in range(1, numbers+1):
    if numbers % i == 0:
        div_set.append(i)
    print(div_set)
