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

    def twoSumBST(self, root, k):
        #your code goes here 
        seen = set()
        def dfs(node):
            if not node:
                return  False
            
            if k - node.val in  seen:
                return True
            seen.add(node.val)

            return dfs(node.right)or dfs(node.left)
        
        return dfs(root)


root = [5, 3, 6, 2, 4, None, 7] 
k = 9
tree = Solution().bstFromPreorder(root)
print(Solution().twoSumBST(tree,k))
root = [5, 3, 6, 2, 4, None, 7] 
k = 12
tree = Solution().bstFromPreorder(root)
print(Solution().twoSumBST(tree,k))
