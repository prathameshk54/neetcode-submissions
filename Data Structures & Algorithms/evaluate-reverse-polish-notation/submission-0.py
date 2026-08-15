class Solution:
    def isSign(self, token):
        if len(token) == 1 and token in '+-*/':
            return True
        else:
            return False
    def operate(self, op1, op2, token):
        if token == '+':
            return op1 + op2
        elif token == '-':
            return op1 - op2
        elif token == '*':
            return op1 * op2
        elif token == '/':
            return int(op1 / op2)

    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for token in tokens:
            if self.isSign(token):
                op2 = stk.pop()
                op1 = stk.pop()
                stk.append(self.operate(op1, op2, token))
            else:
                stk.append(int(token))
        return stk[0]    
        