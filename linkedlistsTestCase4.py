from linkedlists import Node, LinkedLists

llist = LinkedLists(['a', 'b', 'c', 'd'])
print(llist)

# correct e.g.
llist.add_after('c', Node('e'))
print(llist)

# wrong e.g.
llist.add_after('f',Node('d'))
