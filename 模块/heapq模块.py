''''''
'''
heapq模块，提供了优先级队列，即堆
最小堆,以list模拟堆
在list上进行堆操作
list内元素可为元组，依次比较元组内元素
'''
'''
- 序列转化为堆
    - heapq.heapify(list)
- 插入弹出
    - heapq.heappush(heap, num)：插入num
    - heapq.heappop(heap)：弹出最小值，即heap[0]
    - heapq.heapreplace(heap, num)：弹出并插入
    - heapq.heappushpop(heap, num)：插入并弹出
- 通用函数
    - heapq.merge(*iterables, key=None, reverse=False)：将多个已排序输入合并为一个已排序输出，返回值为iterator，类似sorted(itertools.chain(*iterables))
    - heapq.nlargest(n, iterable, key=None)：从iterable提取前n大的元素
'''
from heapq import *

h = [3,5,6,8,1,2]

#原地将列表转为堆
heapify(h)
print(type(h))
print(heappop(h))

print([heappop(h) for _ in range(len(h))])
print(h)

qw = [[2,3,2,4],[12,34,1,3]]
for i in qw:
    heapify(i)
a = list(merge(*qw))
print(a)

h = []
heappush(h, (1, 1, 35))
heappush(h, (1, 2, 35))
heappush(h, (1, 3, 35))
print(h)
print(heappop(h))
print(heappop(h))
print(heappop(h))