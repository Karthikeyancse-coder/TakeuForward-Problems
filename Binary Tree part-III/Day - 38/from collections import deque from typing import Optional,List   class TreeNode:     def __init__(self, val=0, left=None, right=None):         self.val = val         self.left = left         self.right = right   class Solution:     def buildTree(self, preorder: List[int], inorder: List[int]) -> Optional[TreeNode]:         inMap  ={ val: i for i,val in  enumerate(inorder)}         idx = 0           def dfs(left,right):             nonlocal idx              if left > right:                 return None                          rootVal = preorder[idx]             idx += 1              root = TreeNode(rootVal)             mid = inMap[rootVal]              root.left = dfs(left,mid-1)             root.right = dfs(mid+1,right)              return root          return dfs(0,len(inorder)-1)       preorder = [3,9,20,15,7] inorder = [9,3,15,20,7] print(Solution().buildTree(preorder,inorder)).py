from collections import deque
from typing import Optional,List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap  ={ val: i for i,val in  enumerate(inorder)}
        idx = 0 

        def dfs(left,right):
            nonlocal idx 
            if left > right:
                return None
            
            rootVal = preorder[idx]
            idx += 1

            root = TreeNode(rootVal)
            mid = inMap[rootVal]

            root.left = dfs(left,mid-1)
            root.right = dfs(mid+1,right)

            return root

        return dfs(0,len(inorder)-1)

    
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(Solution().buildTree(preorder,inorder))
