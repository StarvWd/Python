# 队列
- collections.deque
    - 在数据结构层面实现 双端队列
    - 可用来实现 栈 或 队列
- queue
    - 基于collections.deque
    - 用于多线程切换
    - 提供三种队列
        - Queue(FIFO)
        - PriorityQueue(优先级队列):基于heapq模块
        - LifoQueue(LIFO)
 
## collections.deque
- deque([iterable[, maxlen]])
    - 从iterable中初始数据，若未指定，队列为空
    - maxlen未指定时，队列可扩展任意长度
    - 若maxlen指定，队列满时，新项加入，另一端的项就会弹出
- append(x)
- appendleft(x)
- pop()
- popleft()
- exend(iterable)
- exendleft(iterable)
- rotate(n=1)
    - n 是正数，向右循环移动 n 步，相当于d.appendleft(d.pop())
    - n 是负数，向左循环移动 n 步，相当于d.append(d.popleft())
- 支持迭代，下标访问，len，count，in

## queue
- queue.Queue(maxsize=0)

 