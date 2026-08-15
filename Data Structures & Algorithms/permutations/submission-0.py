class Solution:
    def rec(self, ps, idx, nums):
        if idx == len(nums):
            self.res.append(ps.copy())
            return
        for i in range(idx, len(nums)):
            nums[i], nums[idx] = nums[idx], nums[i]
            ps.append(nums[idx])
            self.rec(ps, idx + 1, nums)
            ps.pop()
            nums[i], nums[idx] = nums[idx], nums[i]

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.rec([], 0, nums)
        return self.res