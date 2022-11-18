
from typing import Optional

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            # Сохраним ссылку чтобы не потерять при перестановке
            nxt = curr.next
            # Меняем ссылку на след. элемент = предыдущий 
            # Для 1-го элемента, prev = None
            # Для 2-го, prev = 1-й
            curr.next = prev
            prev = curr
            # Делаем текущий = пред.
            curr = nxt

        self.print_llist(prev)

    def print_llist(self, head):
        node = head
        while node:
            print(node.val)
            node = node.next


if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/reverse-linked-list/
        Дано: Дано начало `head` связанного списка
        Необходимо: Вернуть связанный список в обратном порядке
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
    res = solution.reverseList(head)
    solution.print_llist(res)
