from typing import Optional, List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:
    def __init__(self, nodes=Optional[List]):
        self.head = None
        if nodes:
            node = ListNode(nodes.pop(0))
            self.head = node
            for item in nodes:
                node.next = ListNode(item)
                node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass


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
    llist = LinkedList([3, 2, 0, -4])
    print(llist)
    solution = Solution()
    print(solution.hasCycle(llist.head))
