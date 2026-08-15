class Solution:

    def isOpeningBrace(self, ch):
        if ch == '(' or ch == '[' or ch == '{':
            return True
        else:
            return False

    def isMatchingBrace(seld, ob, cb):
        if ob+cb == '()' or ob+cb =='[]' or ob+cb == '{}':
            return True
        else:
            return False

    def isValid(self, s: str) -> bool:
        stk = []
        for brace in s:
            if self.isOpeningBrace(brace):
                stk.append(brace)
            else:
                if len(stk) and self.isMatchingBrace(stk[-1], brace):
                    stk.pop()
                else:
                    return False
        if len(stk):
            return False
        else:
            return True