class Solution:
    def rec(self, nums, i, target, sum_, ps):
        if i == len(nums):
            if sum_ == target:
                self.res.append(ps.copy())
            return
        self.rec(nums, i + 1, target, sum_, ps)
        cnt = 0
        while(sum_ + nums[i] <= target):
            ps.append(nums[i])
            sum_ += nums[i]
            self.rec(nums, i + 1, target, sum_, ps)
            cnt += 1
        for idx in range(cnt):
            ps.pop()
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.rec(nums, 0, target, 0, [])
        return self.res