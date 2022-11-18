from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Если список пустой, то явно не зациклен
        if not head:
            return False

        # В начале 2 указателя ссылаются на начало списка
        slow = fast = head
        # Пока у быстрого указателя есть след. элемент и след. след. - перемещаем указатели
        while fast.next and fast.next.next:
            print(f"fast = {fast.val}; slow = {slow.val}")
            # быстрый на 2 эл.
            fast = fast.next.next
            # медленный на 1
            slow = slow.next
            # Если они встретились - значит список зациклен
            if fast == slow:
                return True

        return False


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/linked-list-cycle/
    Дано: Дано начало `head` связанного списка
    Необходимо: Определить является ли список зациклиным
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    # Input: head = [3,2,0,-4], pos = 1
    node1 = ListNode(3)
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(0)
    node2.next = node3
    node4 = ListNode(-4)
    node3.next = node4
    node5 = ListNode(5)
    node4.next = node2
    # node5.next = None
    solution = Solution()
    print(solution.hasCycle(node1))
