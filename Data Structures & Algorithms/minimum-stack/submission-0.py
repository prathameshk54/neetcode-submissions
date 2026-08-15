class MinStack:

    def __init__(self):
        self.val_stack = []
        self.min_stack = []        

    def push(self, val: int) -> None:
        self.val_stack.append(val)
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        res = self.val_stack.pop()
        if len(self.min_stack) and self.min_stack[-1] == res:
            self.min_stack.pop()

    def top(self) -> int:
        if len(self.val_stack):
            return self.val_stack[-1]
        else:
            return -1

    def getMin(self) -> int:
        if len(self.min_stack):
            return self.min_stack[-1]
        else:
            return -1
