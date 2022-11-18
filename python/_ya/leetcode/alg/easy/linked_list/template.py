
from typing import Optional

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def func(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


    def print_llist(self, head):
        node = head
        nodes = []
        while node:
            nodes.append(str(node.val))
            node = node.next
        print(" -> ".join(nodes))

if __name__ == "__main__":
    """
        Ссылка: 
        Дано: Дано начало `head` связанного списка
        Необходимо: 
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()

    # Input: head = [1,2,3,4,5]
    head = ListNode(1)
    prev = head
    for i in range(2, 6):
        node = ListNode(i)
        prev.next = node
        prev = node

    solution = Solution()
    res = solution.func(head)
    print()
    solution.print_llist(res)
