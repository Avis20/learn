from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Создадим фиктивный список чтоб не заморачиваться с if head is None
        head = ListNode(0)
        node = head
        
        # Пока один из списков не закончится
        while l1 and l2:
            # Если в первом списке эл. меньше            
            if l1.val < l2.val:
                # Добавляем в новый список
                node.next = l1
                # Берем след. из первого списка
                l1 = l1.next
            else:
                # Иначе - 2-й эл. меньше или они равны
                node.next = l2
                l2 = l2.next
            node = node.next

        # Если какой-то список оказался короче - добавим остаток в хвост
        if l1:
            node.next = l1
        if l2:
            node.next = l2

        return head.next

    def print_llist(self, head):
        node = head
        while node:
            print(node.val)
            node = node.next


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/merge-two-sorted-lists/
    Дано: Даны 2 указателя на сортированные связанные списки
    Необходимо: Объединить в 1 связанный сортированный список
    Примечание:
    """
    solution = Solution()

    # Input: head = [1,2,3,4,5]
    head1 = ListNode(1)
    prev = head1
    for i in [2, 4]:
        node = ListNode(i)
        prev.next = node
        prev = node

    head2 = ListNode(1)
    prev = head2
    for i in [3, 4]:
        node = ListNode(i)
        prev.next = node
        prev = node

    last_node = ListNode(5)

    res = solution.mergeTwoLists(head1, head2)
    print("AAA")
    solution.print_llist(res)
