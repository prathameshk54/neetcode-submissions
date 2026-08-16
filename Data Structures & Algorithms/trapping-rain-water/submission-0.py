class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = [0] * n
        rmax = [0] * n

        max_ = 0
        for i in range(n):
            if height[i] > max_:
                max_ = height[i]
            lmax[i] = max_
        
        max_ = 0
        for i in range(n - 1, -1, -1):
            if height[i] > max_:
                max_ = height[i]
            rmax[i] = max_
        
        total_water = 0
        for i in range(n):
            if i == 0:
                lht = 0
            else:
                lht = lmax[i - 1]
            if i == (n - 1):
                rht = 0
            else:
                rht = rmax[i + 1]
            water_ht = min(lht, rht)
            total_water += max(water_ht - height[i], 0)
        
        return total_water