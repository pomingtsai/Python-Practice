# -*- coding: UTF-8 -*-
#題目：有四個數字：1、2、3、4，能組成多少個互不相同且無重複數字的三位元數？各是多少？
#程式分析：可填在百位、十位元、個位的數字都是1、2、3、4。組成所有的排列後再去掉不滿足條件的排列。

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if( i != k ) and (i != j) and (j != k):
                print (i,j,k)