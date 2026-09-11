class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = 1
        right = 1
        for num, i in enumerate(nums):
            res[num] = left
            left *= i
        
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        
        return res