from collections import deque
from typing import Optional,List 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    def Insert(self,root,val):
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self.Insert(root.left,val)

        else:
            root.right = self.Insert(root.right, val)
        
        return root

    def bulidBST(self, vals):
        root = None 
        for val in  vals:
            root  = self.Insert(root, val)
        return root 
    

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if root.val == val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
        

val = [5, 3, 7, 8]
tree = Solution().bulidBST(val)
print(Solution().searchBST(tree,3))

val = [10,4,6,1,3,2,4]
tree = Solution().bulidBST(val)
print(Solution().searchBST(tree,1))

