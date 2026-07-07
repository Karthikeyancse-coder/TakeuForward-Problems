from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildtree(self, values):
        if not values:
            return None

        root = TreeNode(values[0])
        q = deque([root])
        i = 1

        while q and i < len(values):
            node = q.popleft()

            if i < len(values) and values[i] is not None:
                node.left = TreeNode(values[i])
                q.append(node.left)
            i += 1

            if i < len(values) and values[i] is not None:
                node.right = TreeNode(values[i])
                q.append(node.right)
            i += 1

        return root

    def boundary(self, root):
        if root is None:
            return []

        res = [root.val]

        def left(node):
            if node is None:
                return

            # Don't include leaf nodes
            if node.left is None and node.right is None:
                return

            res.append(node.val)

            if node.left:
                left(node.left)
            else:
                left(node.right)

        def lf(node):
            if node is None:
                return

            if node.left is None and node.right is None:
                res.append(node.val)
                return

            lf(node.left)
            lf(node.right)

        def right(node, level):
            if node is None:
                return

            if node.left is None and node.right is None:
                return

            if node.right:
                right(node.right, level + 1)
            else:
                right(node.left, level + 1)

            # Same insertion idea as yours
            res.insert(len(res) - level, node.val)

        left(root.left)
        lf(root)
        right(root.right, 0)

        return res        




p = [1,2,3,4,5,6,7]
# q = [5, 1, 2, 8, None, None, 4, None, 5, None, None, 7 ]
tree1 = Solution().buildtree(p)
print(Solution().boundary(tree1))

# tree2 = Solution().buildtree(q)
# print(Solution().zigzagLevelOrder(tree2))


