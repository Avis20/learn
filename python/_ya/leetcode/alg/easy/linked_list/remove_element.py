
from typing import Optional

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], target: int) -> Optional[ListNode]:
        result = ListNode(0)
        result.next = head

        curr = result
        while curr.next:
            if curr.next.val == target:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return result.next


    def print_llist(self, head):
        node = head
        nodes = []
        while node:
            nodes.append(str(node.val))
            node = node.next
        print(" -> ".join(nodes))

if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/remove-linked-list-elements/
        Дано: Дано начало `head` связанного списка
        Необходимо: Удалить все `target` элементы из списка
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()

    # Input: head = [1,2,3,4,5,3]
    head = ListNode(1)
    prev = head
    for i in range(2, 6):
        node = ListNode(i)
        prev.next = node
        prev = node

    last_node = ListNode(1)
    prev.next = last_node

    solution.print_llist(head)
    solution = Solution()
    res = solution.removeElements(head, 1)
    print()
    solution.print_llist(res)

    print('\n\n')

    # Input: head = [1,2,3,4,5,3]
    head = ListNode(7)
    prev = head
    for i in [7,7,7]:
        node = ListNode(i)
        prev.next = node
        prev = node

    solution.print_llist(head)
    print()
    solution = Solution()
    res = solution.removeElements(head, 7)
    solution.print_llist(res)

