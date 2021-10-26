# BMI(Body Mass Index)值計算公式
# BMI = 體重(公斤) / 身高^2(公尺^2)

import math
height = float(input("請輸入您的身高(cm):"))
weight = float(input("請輸入您的體重(kg):"))

BMI = round((weight / ((height / 100) ** 2)), 1)

if BMI >= 35:
    print("您的BMI值為",BMI,"kg/m\u00b2，是屬於「重度肥胖」！")
elif BMI >= 30 and BMI < 35:
    print("您的BMI值為",BMI,"kg/m\u00b2，是屬於「中度肥胖」！")
elif BMI >= 27 and BMI < 30:
    print("您的BMI值為",BMI,"kg/m\u00b2，是屬於「輕度肥胖」！")
elif BMI >= 24 and BMI < 27:
    print("您的BMI值為",BMI,"kg/m\u00b2，是屬於「過重」！")
elif BMI >= 18.5 and BMI < 24:
    print("您的BMI值為",BMI,"kg/m\u00b2，是屬於「標準」！")
else:
    print("您的BMI值為",BMI,"kg/m\u00b2，是屬於「體重過輕」！")