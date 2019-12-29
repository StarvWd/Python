

''''''
'''
生成器:generator

'''

l = [_ for _ in range(10)]
print(l)


l = (_ for _ in range(10))
print(l)
print(next(l))
for i in l:
    print(i)