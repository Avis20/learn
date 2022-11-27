from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def func(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pass

    def print_tree(self, root):
        pass


if __name__ == "__main__":
    """
    Ссылка:
    Дано: Дано начало `root` бинарного дерева
    Необходимо:
    Примечание:
    Решение:
    Сложность алгоритма:
    """
    solution = Solution()

    root = TreeNode(1)
    node2 = TreeNode(2)
    root.right = node2

    node3 = TreeNode(3)
    node2.left = node3

    node4 = TreeNode(4)
    root.left = node4
    node5 = TreeNode(5)
    node4.left = node5
    node6 = TreeNode(6)
    node4.right = node6
    # node7 = TreeNode(7)
    # node6.left = node7

    print(solution.postorderTraversal(root))
