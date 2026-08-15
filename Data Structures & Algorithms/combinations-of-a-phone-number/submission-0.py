class Solution:
    def rec(self, ps, digits, idx):
        #base condition
        if idx == len(digits):
            self.res.append("".join(ps))
            return
        
        #general case
        for letter in self.map[digits[idx]]:
            ps.append(letter)
            self.rec(ps, digits, idx + 1)
            ps.pop()

    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.map = {
                    "2":"a b c".split(),
                    "3":"d e f".split(),
                    "4":"g h i".split(),
                    "5":"j k l".split(),
                    "6":"m n o".split(),
                    "7":"p q r s".split(),
                    "8":"t u v".split(),
                    "9":"w x y z".split()
                    }
        self.res = []
        self.rec([], digits, 0)
        return self.res
