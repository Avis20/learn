
from typing import Optional

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        # Идем пока есть нода и есть след. нода
        # проверку на node надо сделать т.к. может прийти пустой список
        while node and node.next:
            # Если текущее значение ноды == след.
            if node.val == node.next.val:
                # Переместим указатель на след. элемент
                node.next = node.next.next
            else:
                # Если значения разные - перейдем к след. ноде
                node = node.next
        return head


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
    for i in [1,2,3,3]:
        node = ListNode(i)
        prev.next = node
        prev = node

    solution = Solution()
    solution.print_llist(head)
    res = solution.deleteDuplicates(head)
    print()
    solution.print_llist(res)
