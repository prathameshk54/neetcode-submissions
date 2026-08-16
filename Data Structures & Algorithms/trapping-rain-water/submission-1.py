class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = 0
        rmax = 0
        left = 0
        right = n - 1
        total_water = 0

        while left <= right:
            if lmax < rmax:
                total_water += max(0, lmax - height[left])
                if height[left] > lmax:
                    lmax = height[left]
                left += 1
            else:
                total_water += max(0, rmax - height[right])
                if height[right] > rmax:
                    rmax = height[right]
                right -= 1
        
        return total_water