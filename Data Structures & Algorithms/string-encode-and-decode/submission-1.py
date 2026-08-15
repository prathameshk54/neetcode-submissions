class Solution:

    def encode(self, strs: List[str]) -> str:
        #<#strings>+<start>+<len1>+<len2>+<len3>strings
        encoded_str = str(len(strs)) + '+'
        start = len(encoded_str)
        for str_ in strs:
            start += (1 + len(str(len(str_))))
        if len(str(start + len(str(start)))) == len(str(start)):
            start = start + len(str(start))
        else:
            start = start + len(str(start)) + 1
        encoded_str = encoded_str + str(start)
        for str_ in strs:
            encoded_str = encoded_str + '+' + str(len(str_))
        for str_ in strs:
            encoded_str = encoded_str + str_
        print(encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        temp = 0
        i = 0
        while(s[i] != '+'):
            i += 1
        n = int(s[temp:i])

        i += 1
        temp = i
        while(i < len(s) and s[i] != '+'):
            i += 1
        if i == len(s):
            return []
        start = int(s[temp:i])

        len_ = [0] * n
        for idx in range(n - 1):
            i += 1
            temp = i
            while(s[i] != '+'):
                i += 1
            len_[idx] = int(s[temp:i])
        len_[n - 1] = int(s[i+1:start])

        res = []
        i = start
        for idx in range(n):
            res.append(s[i : (i + len_[idx])])
            i += len_[idx]
        return res  

