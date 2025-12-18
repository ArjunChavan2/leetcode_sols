pairs = {"(": ")", "{": "}", "[": "]"}
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for b in s:
            if b in pairs.keys():
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if pairs[last] != b:
                    return False
        

        return stack == []

# This solution has a time complexity of O(n), where n is the length of the string, s.
# This algorithm is efficient because it processes each character through a stack exactly
# once, leading to a linear relationship between the size of the input and the number of operations performed.
# By using a stack to keep track of opening parentheses, it ensures that each closing parenthesis is matched correctly,
# allowing for quick validation of the entire string.