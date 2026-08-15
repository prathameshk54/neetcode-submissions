import random
class Solution:
    def rec(self, arr, k, start, end):
        pivot = random.randint(start, end - 1)
        arr[start], arr[pivot] = arr[pivot], arr[start]

        #partition the array
        boundary = start

        for i in range(start + 1, end):
            if arr[i][0] <= arr[start][0]:
                arr[i], arr[boundary + 1] = arr[boundary + 1], arr[i]
                boundary += 1
                i += 1
        
        arr[boundary], arr[start] = arr[start], arr[boundary]

        #divide
        if boundary == k:
            return arr[k]
        elif boundary < k:
            return self.rec(arr, k, boundary + 1, end)
        else:
            return self.rec(arr, k, start, boundary)
            
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(points[i][0]**2 + points[i][1]**2, i) for i in range(len(points))]
        
        self.rec(dist, k - 1, 0, len(points))
        res = []
        for i in range(0, k):
            res.append(points[dist[i][1]])
        return res

        