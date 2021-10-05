# 將輸入的秒數轉換成具有時, 分, 秒的時間

total_seconds = int(input("請輸入秒數: "))
hours = total_seconds // 3600
seconds_still_remaining = total_seconds % 3600
minutes = seconds_still_remaining // 60
seconds_finally_remaining = seconds_still_remaining % 60
print("您所輸入的秒數在換後是", hours,"小時", minutes,"分", seconds_finally_remaining,"秒")