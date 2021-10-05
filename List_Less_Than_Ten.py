# 建立一個List，並將小於5的全部列出來在同一列上

number = ' '
number_list = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for number in number_list:
    if number < 5:
        print(number)
