class Solution:
    def rec(self, nums, i, subset):
        if i == len(nums):
            # print(subset)
            self.res.append(subset.copy())
            return
        self.rec(nums, i + 1, subset)
        subset.append(nums[i])
        self.rec(nums, i + 1, subset)
        subset.pop()
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.rec(nums, 0, [])
        return self.res