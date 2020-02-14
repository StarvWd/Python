


'''
- math.ceil         # 向上取整
- math.floor        # 向下取整
- int               # 向0取整（舍弃小数位）
- //                # 向下取整，相当于floor，返回浮点数
- round             # 四舍五入
- math.modf         # 小整分离
'''


import math

a = 2.6
b = -1.4

'''
math.ceil()
严格向上取整，即向数字大的方向
2.6  ->  3
-1.5 -> -1
'''
print(math.ceil(a))
print(math.ceil(b))

'''
math.floor()
严格向下取整，即向数字小的方向
2.6  ->  2
-1.5 -> -2
'''
print(math.floor(a))
print(math.floor(b))

'''
int()
向0方向取整，实际直接抛去小数位
2.6  ->  2
-1.5 -> -1
'''
print(int(a))
print(int(b))

'''
//地板除
严格向下取整，即向数字小的方向，相当于math.floor()
2.6  ->  2
-1.5 -> -2
'''
print(a//1)
print(b//1)

'''
round()
四舍五入
'''
print(round(a))
print(round(b))

'''
math.modf()
分离小数与整数
'''
print(math.modf(a))
print(math.modf(b))