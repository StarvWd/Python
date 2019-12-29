import numpy as np

'''
1.创建
'''
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a)

a = np.random.rand(2,2)
print(a)

b = np.zeros((2,3))
print(b)

c = np.ones((2,3))
print(c)

a = np.empty((2,3))
print(a)

a = np.full((2,3),1)
print(a)
a = np.eye(3,3)
print(a)
#等差数列，左闭右开，0.5表示步长
a = np.arange(1,3,0.5)
print(a)
#等差数列，左闭右闭，5表示个数
b = np.linspace(1,5,5)
print(b)
#等比数列，10^0,10^2,20表示个数
c = np.logspace(0,2,5)
print(c)

#广播机制创建二维数组
a = np.arange(0,60,10).reshape(-1,1) + np.arange(0,6)
print(a)
'''
访问，类似列表，可使用切片，不同在于与原数组是共享同一块数据空间,
'''
x = np.arange(10)
a = x[1:5]
b = x[[0,-1,5]]
print(a.base is x)
print(b.base is x)
print(x)
print(a)
print(b)
#布尔数组访问
x = np.random.rand(6)
print(x)
print(x > 0.5)
print(x[x>0.5])

#多维数组的访问，在[]下标用,分隔；可以使用切片与整数序列,
x = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(x[2,[1,0]])
print(x[0:2,::-1])

a = [i for i in range(10)]
b = a[2:5]
print(a)
print(b)
print(id(a))
print(id(b))

b[0] = 20
print(a)
print(b)
print(id(a))
print(id(b))