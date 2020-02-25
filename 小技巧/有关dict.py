
rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
'''
# 排序字典列表
1. lambda函数
2. operation.itemgetter()
'''

# 1
by_fname = sorted(rows, key = lambda i:i['fname'])
print(by_fname)

by_lfname = sorted(rows, key = lambda i:(i['lname'],i['fname']))
print(by_lfname)
# 2方式稍快一些
from operator import itemgetter
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))
print(rows_by_lfname)