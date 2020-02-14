import queue
from collections import deque


s = [7,8]
s = deque(s, 10)
s.append(9)
s.appendleft(6)
s.extendleft([5,4])
print(s)
