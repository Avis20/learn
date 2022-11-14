from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif not l2 and l1:
            return l1

        head = ListNode(0)
        node = head
        while l1 or l2:
            node1 = ListNode(l1.val)
            node2 = ListNode(l2.val)
            if node1.val == node2.val or node1.val < node2.val:
                node.next = node1
                node.next.next = node2
            else:
                node.next = node2
                node.next.next = node1
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            node = node.next.next

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

    l1_node1 = ListNode(1)
    l1_node2 = ListNode(2)
    l1_node1.next = l1_node2

    l1_node3 = ListNode(4)
    l1_node2.next = l1_node3
    head_node1 = l1_node1

    l2_node1 = ListNode(1)
    l2_node2 = ListNode(3)
    l2_node1.next = l2_node2

    l2_node3 = ListNode(4)
    l2_node2.next = l2_node3
    head_node2 = l2_node1

    res = solution.mergeTwoLists(head_node1, head_node2)
    while res:
        print(res.val)
        res = res.next



    # l2_node1 = ListNode(0)
    # head_node2 = l2_node1


    # res = solution.mergeTwoLists(None, head_node2)
    # while res:
    #     print(res.val)
    #     res = res.next
