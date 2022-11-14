from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/middle-of-the-linked-list/
    Дано: Дано начало `head` связанного списка
    Необходимо: Определить является ли список зациклиным
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    # Input: head = [1,2,3,4,5]
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2

    node3 = ListNode(3)
    node2.next = node3

    node4 = ListNode(4)
    node3.next = node4

    node5 = ListNode(5)
    node4.next = node5

    node0 = ListNode(0)
    node5.next = node0

    # node = node1
    # while node.next:
    #     print(node.val)
    #     node = node.next

    solution = Solution()
    res = solution.middleNode(node1)
    while res.next:
        print(res.val)
        res = res.next
