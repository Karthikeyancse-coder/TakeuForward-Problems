from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def buildtree(self,value):
        if not value:
            return None
        root = TreeNode(value[0])
        q = deque([root])
        i = 1 
        while q and i < len(value):
            node = q.popleft()
            
            if i < len(value) and value[i] is not None:
                node.left = TreeNode(value[i])
                q.append(node.left)
            i+=1
            if i < len(value) and value[i] is not None:
                node.right = TreeNode(value[i])
                q.append(node.right)
            i+=1
        return root 
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if node is  None:
                return 0
            left = dfs(node.left)
            if left == -1:
                return -1

            right = dfs(node.right)
            if right == -1:
                return -1

            if abs(left - right) > 1:
                return -1

            return 1 + max(left,right)
        
        return dfs(root) != -1
                  

root = [1, 2, None, 4, 5,6,7,8]
tree = Solution().buildtree(root)
print(Solution().isBalanced(tree))

root = [3,9,20,None,None,15,7]
tree = Solution().buildtree(root)
print(Solution().isBalanced(tree))

