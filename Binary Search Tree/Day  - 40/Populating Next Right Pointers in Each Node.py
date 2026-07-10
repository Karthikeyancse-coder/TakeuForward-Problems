from collections import deque
from typing import Optional,List 


class TreeNode:
    def __init__(self, val=0, left=None, right=None,next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

        
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

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        def dfs(node):
            if node is  None or node.left is  None:
                return 
            
            node.left.next = node.right

            if node.next:

                node.right.next = node.next.left
            
            dfs(node.left) 
            dfs(node.right)
        dfs(root)
        return root 



val = [5, 3, 7, 8]
tree = Solution().bulidBST(val)
print(Solution().connect(tree))

val = [10,4,6,1,3,2,4]
tree = Solution().bulidBST(val)
print(Solution().connect(tree))
