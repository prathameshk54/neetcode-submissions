class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        for ch in t:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        
        i = 0
        j = 0
        len_ = 0
        min_ = len(s) + 1
        lidx = -1
        ridx = -1
        cnt = 0
        n = len(t)

        while(1):
            if cnt < n:
                if j >= len(s):
                    break
                if s[j] in d:
                    if d[s[j]] > 0:
                        cnt += 1
                    d[s[j]] -= 1
                j += 1    
                continue
            else:
                len_ = j - i
                if len_ <= min_:
                    min_ = len_
                    lidx = i
                    ridx = j
                if s[i] in d:
                    if d[s[i]] >= 0:
                        cnt -= 1
                    d[s[i]] += 1
                i += 1
        if min_ == len(s) + 1:
            return ""
        else:
            return s[lidx:ridx]
