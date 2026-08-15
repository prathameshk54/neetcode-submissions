import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stones[i] * -1 for i in range(len(stones))]
        heapq.heapify(stones)

        while(len(stones) > 1):
            s1 = -1 * heapq.heappop(stones)
            s2 = -1 * heapq.heappop(stones)
            if s1 - s2 > 0:
                heapq.heappush(stones, -1 * (s1 - s2))

        if len(stones):
            return stones[0] * -1
        else:
            return 0