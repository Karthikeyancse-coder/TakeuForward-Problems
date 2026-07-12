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
            if val is not None:
                root = self.Insert(root,val)
        return root 

    def kLargestSmall(self, root, k):
        #your code goes here
        res = []
        def dfs(node):                    
            if node is None:
                return 
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return [res[k-1],res[-k]]
    

val = [3,1,4,None,2]
key = 1
tree = Solution().bstFromPreorder(val)
print(Solution().kLargestSmall(tree,key))
