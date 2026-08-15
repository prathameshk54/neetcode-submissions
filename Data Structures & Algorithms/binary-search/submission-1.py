class Solution:
    def bin_search(self, left, right, nums, target):
        if left >= right:
            return left if nums[left] == target else -1
        mid = int(left + (right - left) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.bin_search(mid + 1, right, nums, target)
        else:
            return self.bin_search(left, mid - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
        return self.bin_search(0, len(nums) - 1, nums, target)