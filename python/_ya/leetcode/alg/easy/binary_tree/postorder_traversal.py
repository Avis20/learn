from typing import Optional, List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def helper(node):
            if node:
                helper(node.left)
                helper(node.right)
                res.append(node.val)

        helper(root)
        return res


if __name__ == "__main__":
    """
    Ссылка: https://leetcode.com/problems/binary-tree-postorder-traversal/
    Дано: Дано начало `root` бинарного дерева
    Необходимо: вернуть все элементы дерева в обратном порядке
    Пример:
        Input: root = [1,null,2,3]
                1
                 \
                  2
                 /
                3 
        
        Output: [3,2,1]

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
