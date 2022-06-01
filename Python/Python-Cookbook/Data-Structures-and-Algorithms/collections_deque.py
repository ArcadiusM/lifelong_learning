# Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and
# the queue is full, the oldest item is automatically removed. For example:
from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

# More generally, a deque can be used whenever you need a simple queue structure. If
# you don’t give it a maximum size, you get an unbounded queue that lets you append
# and pop items on either end. For example:
q = deque()
q.append(1)
q.append(2)
q.append(3)
q.appendleft(4)
print(q)

# Adding or popping items from either end of a queue has O(1) complexity. This is unlike
# a list where inserting or removing items from the front of the list is O(N).

