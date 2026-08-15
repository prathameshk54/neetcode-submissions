class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i, s in enumerate(strs):
            sd = [0] * 26
            for ch in s:
                sd[ord(ch) - ord('a')] += 1
            if tuple(sd) in d:
                d[tuple(sd)].append(i)
            else:
                d[tuple(sd)] = [i]
        
        res = []
        for key in d.keys():
            grp = []
            for idx in d[key]:
                grp.append(strs[idx])
            res.append(grp.copy())
        
        return res
                