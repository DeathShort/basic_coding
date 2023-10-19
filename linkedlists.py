class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return self.data


class LinkedLists:
    def __init__(self, nodes: list = None) -> None:
        '''init linkedlist, if nodes is not None ,then build linkedlist'''
        self.head = None
        if nodes is not None:
            node = Node(nodes.pop(0))
            self.head = node
            for data in nodes:
                node.next = Node(data)
                node = node.next

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self) -> str:

        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ','.join(nodes)

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_last(self, node: Node):
        if self.head is None:
            self.head = node
            return
        for currentNode in self:
            pass
        currentNode.next = node

    def add_after(self, targetNodeData: str, node: Node):
        '''find the node, and insert a new node after it'''
        if self.head is None:
            raise Exception("List is empty")
        for elem in self:
            if elem.data == targetNodeData:
                node.next = elem.next
                elem.next = node
                return
        raise Exception(
            f'List do not find node which data is {targetNodeData}')

    def add_before(self, targetNodeData: str, node: Node):
        '''find the node, and insert a new code before it'''
        if self.head is None:
            raise Exception('List is empty')

        if self.head.data == targetNodeData:
            self.add_first(node)
            return

        beforNode = None
        for elem in self:
            if elem.data == targetNodeData:
                beforNode.next = node
                node.next = elem
                return
            beforNode = elem
        raise Exception(
            f'List do not find node which data is {targetNodeData}')

    def remove_node(self, targetNodeData: str):
        '''remove the target data'''

        if self.head is None:
            raise 'list is empty'

        if self.head.data == targetNodeData:
            self.head = self.head.next
            return

        previousNode = None
        for elem in self:
            if elem.data == targetNodeData:
                previousNode.next = elem.next
                return
            previousNode = elem

        raise Exception(
            f'List do not find node which data is {targetNodeData}')
