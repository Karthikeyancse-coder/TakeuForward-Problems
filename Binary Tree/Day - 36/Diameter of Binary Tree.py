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
    
    def diameterOfBinaryTree(self, root):
        depth = [0] 
        self.height(root,depth)
        return depth[0]
    
    def  height(self,root,depth):
        if root is None:
            return 0
        
        lh = self.height(root.left,depth)
        rh = self.height(root.right,depth)

        depth[0] = max(depth[0], lh + rh)

        return 1 + max(lh,rh)

         

root = [1, 2, None, 4, 5,6,7,8]
tree = Solution().buildtree(root)
print(Solution().diameterOfBinaryTree(tree))

