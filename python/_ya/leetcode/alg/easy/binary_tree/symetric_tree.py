from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def helper(node_left, node_right):

            if not node_left and not node_right:
                return True

            print(f"node_left {node_left.val} and node_right {node_right.val}")

            if not node_left or not node_right:
                return False

            return node_left.val == node_right.val and \
                helper(node_left.left, node_right.right) and \
                helper(node_left.right, node_right.left)
            
        return helper(root, root)



def tree_6():
    """
            1
           / \
          /   \
         2     2
        / \   / \
       3   4 5   3
    """
    root = TreeNode(1)
    node1, node2 = TreeNode(2), TreeNode(2)
    root.left, root.right = node1, node2

    node3, node4 = TreeNode(3), TreeNode(4)
    node1.left, node1.right = node3, node4

    node3, node4 = TreeNode(5), TreeNode(3)
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
    """
    Ссылка:
    Дано: Дано начало `root` бинарного дерева
    Необходимо: Проверить симетричное ли дерево
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()


    print(solution.isSymmetric(tree_6()))

