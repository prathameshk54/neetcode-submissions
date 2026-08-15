import random
class Solution:      
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        n = len(nums)
        freq = []
        for i in range(n + 1):
            freq.append([])
        for num in d.keys():
            freq[d[num]].append(num)

        count = 0
        res = []
        for i in range(n,-1,-1):
            if count == k:
                break
            rem = min(len(freq[i]), k - count)
            while rem > 0:
                res.append(freq[i][rem - 1])
                rem -= 1
                count += 1
        
        return res