
from typing import Optional

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        node = head
        num = node.val
        while node.next:
            num = num * 2 + node.next.val
            node = node.next
        return num



    def print_llist(self, head):
        node = head
        nodes = []
        while node:
            nodes.append(str(node.val))
            node = node.next
        print(" -> ".join(nodes))

if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
        Дано: Дано начало `head` связанного списка состоящего из 0 и 1
        Необходимо: конвертировать связанный список в целое число
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()

    head = ListNode(1)
    prev = head
    for i in [0,1]:
        node = ListNode(i)
        prev.next = node
        prev = node

    solution = Solution()
    print(solution.getDecimalValue(head))
