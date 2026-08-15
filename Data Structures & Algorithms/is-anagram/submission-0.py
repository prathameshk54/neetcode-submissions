class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        for ch in t:
            if ch not in d:
                return False
            if d[ch] == 0:
                return False
            d[ch] -= 1
        for ch in d.keys():
            if d[ch] > 0:
                return False
        return True