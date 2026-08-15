class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        d = {}

        for ch in s1:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        count = 0
        i = 0
        j = 0

        while(j < len(s2)):
            if s2[j] in d and d[s2[j]] > 0:
                count += 1
                d[s2[j]] -= 1
                j += 1
                if count == n:
                    return True
                continue
            if i < j:
                d[s2[i]] += 1
                i += 1
                count -= 1  
            else:
                if s2[i] not in d or d[s2[i]] == 0:
                    i += 1
                    if i == len(s2):
                        break
                else:
                    d[s2[i]] -= 1
                    count += 1
                    j = i + 1

        if count == n:
            return True
        else:
            return False