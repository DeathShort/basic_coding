from linkedlists import Node, LinkedLists

llist = LinkedLists(['a', 'b', 'c', 'd'])
print(llist)

# correct e.g.
llist.add_before('c', Node('e'))
print(llist)

# wrong e.g.
llist.add_before('f', Node('d'))
