# Description: This file demonstrates the use of assert statements in Python.
# Author: Wang Yong
# email: dr.yongwang at hotmail.com
# Date: 2023/11/15



def add(a, b):
    return a + b

# 如返回值为True，则不会有任何提示，程序继续执行，否则会抛出异常
assert(add(1, 2) == 3)
assert(add(1.0, 2.0) == 3.0)
assert(add("1", "2") == "12")
a = 1
b = 3
assert a > 0 and b == 3, "表达式应为true"
# 如果assert后面的表达式为False，则抛出异常，程序终止。测试表达式为False的情况, 应写成 (express) == False
assert not (a > 0 and b == 3) == False, "表达式应为false"
print(not(a > 0 and b == 3)==False)