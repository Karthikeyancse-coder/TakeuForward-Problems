from collections import deque
from typing import Optional,List 


class TreeNode:
    def __init__(self, val=0, left=None, right=None,next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

        
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def bulid(left , right):
            if left > right:
                return None
            
            mid = left +(right - left)//2
            root = TreeNode(nums[mid])
            root.left = bulid(left, mid - 1)
            root.right = bulid(mid +1 , right)
        
            return root
        return bulid(0,len(nums) -1 ) 


val = [-10,-3,0,5,9]
# tree = Solution().bulidBST(val)
print(Solution().sortedArrayToBST(val))

val = [1,3]
# tree = Solution().bulidBST(val)
print(Solution().sortedArrayToBST(val))
