class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        max_ = -1
        d = {s[0] : 1}

        i = 0
        j = 1
        len_ = 1

        while(j < len(s)):
            if s[j] not in d or d[s[j]] == 0:
                len_ += 1
                if s[j] in d:
                    d[s[j]] += 1
                else:
                    d[s[j]] = 1
                j += 1
                continue
            if len_ > max_:
                max_ = len_
            d[s[i]] -= 1
            i += 1
            len_ -= 1
        if len_ > max_:
            max_ = len_    
        return max_

        