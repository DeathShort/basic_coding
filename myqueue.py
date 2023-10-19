
# create queue use list
myqueue = []
myqueue.append('a')
myqueue.append('b')
myqueue.append('c')

print(myqueue)
print(myqueue.pop(0))
print(myqueue.pop(0))
print(myqueue.pop(0))

print(myqueue)

# create queue use collections deque
from collections import deque

myqueue2 = deque()
myqueue2.append('a')
myqueue2.append('b')
myqueue2.append('c')

print(myqueue2)
print(myqueue2.popleft())
print(myqueue2.popleft())
print(myqueue2.popleft())

print(myqueue2)

# create queue use queue Queue
from queue import Queue
q = Queue(maxsize=3)
print(q.qsize())

q.put('a')
q.put('b')
q.put('c')

print(q.full())

print(q.get())
print(q.get())
print(q.get())

print(q.empty())

