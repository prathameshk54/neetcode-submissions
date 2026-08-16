class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = False
        
        max_streak = 0
        for num in d.keys():
            if d[num]:
                continue

            streak = 1
            d[num] = True
            temp = num - 1
            while temp in d:
                d[temp] = True
                streak += 1
                temp -= 1
            temp = num + 1
            while temp in d:
                d[temp] = True
                streak += 1
                temp += 1
            if streak > max_streak:
                max_streak = streak
        
        return max_streak