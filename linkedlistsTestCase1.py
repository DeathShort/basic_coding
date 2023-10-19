from linkedlists import Node, LinkedLists

llist = LinkedLists()

print(llist)
firstNode = Node('a')
secondNode = Node('b')
thirdNode = Node('c')

llist.head = firstNode
print(llist)

firstNode.next = secondNode
secondNode.next = thirdNode
print(llist)