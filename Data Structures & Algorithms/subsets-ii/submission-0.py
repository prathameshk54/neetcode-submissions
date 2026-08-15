class Solution:
    def rec(self, nums, idx, ps):
        #base condition
        if idx == len(nums):
            self.res.append(ps.copy())
            return

        #general recursive conditions
        #include element
        ps.append(nums[idx])
        self.rec(nums, idx + 1, ps)
        ps.pop()

        #skip element
        i = idx + 1
        while(i < len(nums) and nums[i] == nums[idx]):
            i += 1
        self.rec(nums, i, ps)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums = sorted(nums)
        print(nums)
        self.rec(nums, 0, [])
        return self.res

        