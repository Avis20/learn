# breadth-first search, BFS = Поиск в ширину
# https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B8%D1%81%D0%BA_%D0%B2_%D1%88%D0%B8%D1%80%D0%B8%D0%BD%D1%83

from collections import deque


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bfs(self, root):

        q = deque([root])

        levels = []
        while q:
            level = []
            for i in range(len(q)):

                curr = q.popleft()
                level.append(curr.val if curr else None)
                
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
            levels.append(level)

        return levels


def tree_6():
    """
            1
           / \
          /   \
         2     2
        / \   / \
       3   4 5   6
    """
    root = TreeNode(1)
    node1, node2 = TreeNode(2), TreeNode(2)
    root.left, root.right = node1, node2

    node3, node4 = TreeNode(3), TreeNode(4)
    node1.left, node1.right = node3, node4

    node3, node4 = TreeNode(5), TreeNode(6)
    node2.left, node2.right = node3, node4

    return root

def tree_3():
    """
            1
           / \
          /   \
         2     2
        / \   / \
           3     3
    
    """
    root = TreeNode(1)
    node1, node2 = TreeNode(2), TreeNode(2)
    root.left, root.right = node1, node2

    node3, node4 = TreeNode(3), TreeNode(3)
    node1.right, node2.right = node3, node4
    return root

if __name__ == "__main__":
    solution = Solution()
    print(solution.bfs(tree_6()))
    print(solution.bfs(tree_3()))
