
class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

def reverse_llist(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

if __name__ == '__main__':
    node1 = Node(1)
    prev = node1
    for i in range(2, 7):
        node = Node(i)
        prev.next = node
        prev = node

    node = reverse_llist(node1)
    while node:
        print(node.val)
        node = node.next

