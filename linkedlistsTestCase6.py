from linkedlists import Node, LinkedLists

llist = LinkedLists(['a', 'b', 'c', 'd'])
print(llist)

# correct e.g.
llist.remove_node('c')
print(llist)

# correct e.g.
llist.remove_node('a')
print(llist)

# wrong e.g.
llist.remove_node('a')
