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
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        x = float('-inf')
        def dfs(node):
            nonlocal x 
            if node is None:
                return 0
            
            left  = max(0,dfs(node.left))
            right = max(0, dfs(node.right))

            x = max(x , left + right + node.val)
            return node.val + max(left,right)
        
        dfs(root)
        return x 
    
    
p = [1,2,3]
tree1 = Solution().buildtree(p)
print(Solution().maxPathSum(tree1))

q = [-10,9,20,None,None,15,7]
tree2 = Solution().buildtree(q)
print(Solution().maxPathSum(tree2))

