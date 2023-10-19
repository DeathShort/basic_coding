# models to build stack
# list
# collections.deque
# queue.Lifoqueue

# 1. use list to create a stack
# list 有一些缺点。最大的问题是，随着它的增长，它可能会遇到速度问题。 list 中的项目存储的目的是提供对 list 中随机元素的快速访问。从较高层面来说，这意味着这些项目在内存中彼此相邻存储
# 如果你的堆栈变得比当前容纳它的内存块大，那么 Python 需要进行一些内存分配。这可能会导致某些 .append() 调用比其他调用花费更长的时间
# 您永远不应该将 list 用于可以由多个线程访问的任何数据结构。 list 不是线程安全的。
# myStack = []
# myStack.append('a')
# myStack.append('b')
# myStack.append('c')
# print(myStack)
# print(myStack.pop())
# print(myStack.pop())
# print(myStack.pop())
# print(myStack.pop())

# 2. use collections.deque to create a stack
# deque 是建立在双向链表之上的。在链表结构中，每个条目都存储在自己的内存块中，并具有对列表中下一个条目的引用。
# 双向链表与此相同，只是每个条目都引用列表中的上一个条目和下一个条目。这使您可以轻松地将节点添加到列表的任一端。
# 然而，这种在堆栈上恒定时间添加和删除条目需要权衡。获取 myDeque[3] 比获取列表慢，因为 Python 需要遍历列表的每个节点才能到达第三个元素。
# 幸运的是，您很少想在堆栈上进行随机索引或切片。堆栈上的大多数操作都是 push 或 pop 。
# 如果您的代码不使用线程，则恒定时间 .append() 和 .pop() 操作使 deque 成为实现 Python 堆栈的绝佳选择。
#  deque 的文档，它清楚地指出 .append() 和 .pop() 操作都是原子操作，这意味着它们不会被不同的操作中断线。
# from collections import deque

# mystack = deque()
# mystack.append('a')
# mystack.append('b')
# mystack.append('c')
# print(mystack)
# print(mystack.pop())
# print(mystack.pop())
# print(mystack.pop())
# print(mystack.pop())

# 3. use queue.LifoQueue to create a stack
from queue import LifoQueue

mystack = LifoQueue()
mystack.put('a')
mystack.put('b')
mystack.put('c')
print(mystack)
print(mystack.get())
print(mystack.get())
print(mystack.get())
print(mystack.get())