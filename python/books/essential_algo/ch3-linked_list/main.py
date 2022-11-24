class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head: Node | None = None):
        self.head = head

    def add_after(self, search_val: int, new_node: Node):
        node = self.head
        while node:
            if node.val == search_val:
                new_node.next = node.next
                node.next = new_node
                return None
            node = node.next
        raise Exception("Node Not Found")

    def add_last(self, new_node: Node):
        # Создадим фиктивную ноду чтобы не проверять is none в конце
        # Даже если у нас пустой список, node.next не сломается
        dummy = Node(..., next=self.head)
        node = dummy
        while node.next:
            node = node.next
        node.next = new_node
        self.head = dummy.next

    def add_first(self, new_node: Node):
        new_node.next = self.head
        self.head = new_node

    def __repr__(self):
        nodes = []
        node = self.head
        while node:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def print_llist(self) -> None:
        node = self.head
        while node:
            print(node.val)
            node = node.next

    def find_before(self, target: int) -> Node | None:
        dummy = Node(..., next=self.head)
        node = dummy
        while node.next:
            if node.next.val == target:
                return node.next
            node = node.next
        return None

    def find(self, target) -> Node | None:
        node = self.head
        while node:
            if node.val == target:
                return node
            node = node.next
        return None


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2

    node3 = Node(3)
    node2.next = node3

    llist = LinkedList(node1)
    llist.print_llist()
    print(llist.find(3))
    print(llist.find_before(3))
    print(llist)
    llist.add_first(Node(4))
    print(llist)
    llist.add_last(Node(6))
    print(llist)
    llist.add_after(1, Node(7))
    print(llist)
