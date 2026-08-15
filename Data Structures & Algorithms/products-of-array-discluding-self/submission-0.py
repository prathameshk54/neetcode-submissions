class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = []
        p = 1
        for num in nums:
            p *= num
            lprod.append(p)
        
        rprod = [0] * len(nums)
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            p *= nums[i]
            rprod[i] = p
        
        res = []
        for i, num in enumerate(nums):
            left = lprod[i - 1] if i > 0 else 1
            right = rprod[i + 1] if i < len(nums) - 1 else 1
            res.append(left * right)
        
        return res