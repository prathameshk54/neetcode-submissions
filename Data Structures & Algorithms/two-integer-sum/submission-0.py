class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if n in d:
                d[n].append(i)
            else:
                d[n] = [i]
        for i, n in enumerate(nums):
            if target - n not in d:
                continue
            if target - n == n:
                if len(d[n]) <= 1:
                    continue
                else:
                    return [d[n][0], d[n][1]]
            else:
                if i < d[target - n][0]:
                    return [i, d[target - n][0]]
                else:
                    return [d[target - n][0], i]
