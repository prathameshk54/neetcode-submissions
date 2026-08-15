import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_hp = [(nums[i] * -1, i) for i in range(k)]
        heapq.heapify(max_hp)
        res = []
        for i in range(k,len(nums)+1):
            while(1):
                (val, idx) = max_hp[0]
                if idx >= i - k:
                    break
                else:
                    heapq.heappop(max_hp)
            res.append(val * -1)
            if i < len(nums):
                heapq.heappush(max_hp, (nums[i] * -1, i))
        return res