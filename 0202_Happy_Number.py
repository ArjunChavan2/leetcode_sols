def s(n):
    l = str(n)
    n = 0
    for c in l:
        n += int(c) **2
    return n

class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        fast = n
        slow = s(fast)

        while fast != slow != 1:
            fast = s(fast)
            slow = s(s(slow))
        
        return fast != slow