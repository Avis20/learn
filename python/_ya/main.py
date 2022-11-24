class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class CyrcleLinkedList:
    def __init__(self, nodes: list | None):
        self.head = None
        if nodes:
            node = Node(nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = Node(item)
                node = node.next
            node.next = self.head

    def print_list(self, start_point=None):
        nodes = []
        for node in self.traverse(start_point):
            nodes.append(str(node.data))
        print(" -> ".join(nodes))

    def traverse(self, start_point=None):
        if start_point is None:
            start_node = self.head
        else:
            start_node = self.find(start_point)

        node = start_node
        while node and node.next != start_node:
            yield node
            node = node.next
        yield node

    def find(self, target) -> Node | None:
        node = self.head
        while node:
            if node.data == target:
                return node
            node = node.next
        return None


if __name__ == "__main__":
    cllist = CyrcleLinkedList([1, 2, 3, 4])
    cllist.print_list()
    cllist.print_list(2)
    cllist.print_list(4)
    # print(cllist)
