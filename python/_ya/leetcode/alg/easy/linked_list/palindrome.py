from typing import Optional

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.middleLinkedList(head)
        rev = self.reverseLinkedList(mid)
        curr = head
        while rev:
            if rev.val != curr.val:
                return False
            curr = curr.next
            rev = rev.next
        return True

    def middleLinkedList(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
    
    def reverseLinkedList(self, head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev



    def print_llist(self, head):
        node = head
        nodes = []
        while node:
            nodes.append(str(node.val))
            node = node.next
        print(" -> ".join(nodes))

if __name__ == "__main__":
    """
        Ссылка: https://leetcode.com/problems/palindrome-linked-list/description/
        Дано: Дано начало `head` связанного списка
        Необходимо: Проверить является ли связанный список палиндромом
        Примечание:
        Решение: 
        Сложность алгоритма:
    """
    solution = Solution()

    # Input: head = [1,2,3,4,5]
    head = ListNode(1)
    prev = head
    for i in [2,3,4,4,3,2,1]:
        node = ListNode(i)
        prev.next = node
        prev = node

    solution = Solution()
    solution.print_llist(head)
    res = solution.isPalindrome(head)
    print(res)
