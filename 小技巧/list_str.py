
''''''
'''
将列表[]转换成字符串
[1,2,3,4] ->  '1234'
'''
a = [1,2,3]
b = ''.join(list(map(str,a)))
print(b)

'''
数字str转list
'1234' ->  [1,2,3,4]
'''

a = '1 2 3 4'
b = list(map(int,a.split()))
print(b)