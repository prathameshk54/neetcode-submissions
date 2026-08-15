class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while (len(stk) and temp > stk[-1][1]):
                (idx, val) = stk.pop()
                res[idx] = i - idx
            stk.append((i, temp))
        return res