'''

zip函数的使用：
a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]
c = zip(a,b)
    将a,b对应压缩成元祖
    [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
d = zip(*c)
    将c对应解压，相当于转置
    [('a', 'b', 'c', 'd'), (1, 2, 3, 4)]
'''
# 注： 迭代器只能使用一次


a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4]
c = zip(a, b)
print(c)
print(type(c))
print(list(c))

print(list(c))

d = zip(*c)
#print（d）
print(type(d))
print(list(d))