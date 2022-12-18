from typing import Optional


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        deque = [(root, 1)]
        while deque:
            node, depth = deque.pop(0)

            if not node.left and not node.right:
                return depth

            if node.left:
                deque.append((node.left, depth + 1))
            if node.right:
                deque.append((node.right, depth + 1))



    def minDepth2(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        min_level = None
        level = 0
        levels = []
        deque = [root]
        while deque:
            level += 1
            values = []
            nodes = deque.copy()
            for node in nodes:
                deque.pop(0)
                values.append(node.val)
                if not node.left and not node.right:
                    if min_level is None:
                        min_level = level
                    else:
                        min_level = min(min_level, level)
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)

            levels.append(values)
        print(levels)
        return min_level


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

    print(solution.minDepth(root))
