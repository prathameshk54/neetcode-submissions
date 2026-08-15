import random
class Solution:
    def quick_select(self, arr, k, start, end):
        if end <= start:
            return
        
        pivot = random.randint(start, end - 1)
        arr[start], arr[pivot] = arr[pivot], arr[start]

        boundary = start
        for i in range(start + 1, end):
            if arr[i][0] > arr[start][0]:
                continue
            else:
                boundary += 1
                arr[boundary], arr[i] = arr[i], arr[boundary]
        arr[start], arr[boundary] = arr[boundary], arr[start]

        if k > boundary:
            self.quick_select(arr, k, boundary + 1, end)
        elif k < boundary:
            self.quick_select(arr, k, start, boundary)
        else:
            return
            
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1

        freq = []
        for num in d.keys():
            freq.append((d[num], num))
        
        self.quick_select(freq, len(freq) - k, 0, len(freq))
        res = []
        for i in range(len(freq) - k, len(freq)):
            res.append(freq[i][1])
        return res