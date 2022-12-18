
from typing import Optional

class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        queue = [root]
        levels = []
        while queue:
            level = []
            nodes = queue.copy()
            for node in nodes:
                queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            levels.append(level)

        return sum(levels[-1])




if __name__ == '__main__':
    
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)

    node1.left = node2
    node1.right = node3

    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2.left = node4
    node2.right = node5

    node6 = TreeNode(6)
    node3.right = node6

    node7 = TreeNode(7)
    node4.left = node7

    node8 = TreeNode(8)
    node6.right = node8

    solution = Solution()
    print(solution.deepestLeavesSum(node1))