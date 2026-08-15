class Solution:
    def rec(self, nums, idx, ps, target, sum_):
        if sum_ == target:
            self.res.append(ps.copy())
            return
        
        if idx == len(nums):
            return

        cnt = 0
        self.rec(nums, idx + 1, ps, target, sum_)
        for i in range(nums[idx][1]):
            if sum_ + nums[idx][0] > target:
                return
            ps.append(nums[idx][0])
            sum_ += nums[idx][0]
            cnt += 1
            self.rec(nums, idx + 1, ps, target, sum_)
        for i in range(cnt):
            ps.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        map_ = {}
        for cand in candidates:
            if cand not in map_:
                map_[cand] = 1
            else:
                map_[cand] += 1
        
        self.res = []

        nums = [(key, map_[key]) for key in map_]
        sorted(nums, key = lambda x : x[0])

        self.rec(nums, 0, [], target, 0)
        return self.res