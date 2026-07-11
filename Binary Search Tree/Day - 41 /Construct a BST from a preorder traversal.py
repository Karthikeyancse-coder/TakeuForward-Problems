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
            root.right = self.Insert(root.right,val)

        return root 


    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = None
        for val in preorder:
            root = self.Insert(root,val)

        return root 
    
    def inorder(self,root):
        res = [] 
        def dfs(node):
            if node is None:
                return 
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return res


    

val = [8,5,1,7,10,12]
tree = Solution().bstFromPreorder(val)
print(Solution().inorder(tree))

val = [1,3]
tree = Solution().bstFromPreorder(val)
print(Solution().inorder(tree))
