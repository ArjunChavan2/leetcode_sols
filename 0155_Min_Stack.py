class MinStack:

    def __init__(self):
        self.stack = []
        self.memo = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.memo:
            self.memo.append(val)
        else:
            self.memo.append(min(val, self.getMin()))

    def pop(self) -> None:
        del self.stack[-1]
        del self.min_stack[-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

# This solution runs in O(1) time for every function and O(n) memory. The logic behind push
# is that any time the current minimum value is pushed into the min_stack instead of the 
# val, when the val is popped, the minimum value that was pushed with it is still in the
# stack when it was originally pushed and remains there now. This push function uses a 
# memoization vector since it calculates the minimum value of the stack at each push.