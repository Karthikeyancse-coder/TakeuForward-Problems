class Solution:
    def nextPermutation(self, nums):

        n = len(nums)

        for i in range(n - 2, -1, -1):   

            if nums[i] < nums[i + 1]:

                nums[i + 1], nums[i] = nums[i], nums[i + 1]
                nums[i + 1:] = sorted(nums[i + 1:])
                return

        nums.sort()
