from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def func(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0

        deque = [root]
        levels = []
        while deque:
            level = []

            nodes = deque.copy()
            for node in nodes:
                deque.pop(0)
                level.append(node.val)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            levels.append(level)
        
        return sum(levels[-1])


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

    root = TreeNode(3)
    node2 = TreeNode(9)
    root.right = node2

    node3 = TreeNode(20)
    root.left = node3

    node4 = TreeNode(15)
    node3.left = node4
    node5 = TreeNode(7)
    node3.right = node5
    # node6 = TreeNode(6)
    # node4.right = node6
    # node7 = TreeNode(7)
    # node6.left = node7

    print(solution.func(root))
