class Solution:
    def rec(self, ob, cb, nstk, blist):
        if ob == 0 and cb == 0:
            self.res.append("".join(blist))
            return
        if ob > 0:
            blist.append('(')
            self.rec(ob - 1, cb, nstk + 1, blist)
            blist.pop()
        if cb > 0 and nstk > 0:
            blist.append(')')
            self.rec(ob, cb - 1, nstk - 1, blist)
            blist.pop()
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.rec(n, n, 0, [])
        return self.res