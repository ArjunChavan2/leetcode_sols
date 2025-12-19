class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum = str(int(a) + int(b))
        sum = [0] + [int(d) for d in sum]
        for i in range(len(sum) - 1, -1, -1):
            if sum[i] > 1:
                sum[i] = sum[i] % 2
                sum[i-1] += 1

        for i in range(len(sum)):
            sum[i] = str(sum[i])
        if sum[0] == "1":
            return "".join(sum)
        else:
            return "".join(sum[1:])

# This solution runs in O(n) time and uses O(n) space. It adds two binary strings
# by converting them to integers, adding them, and then converting the result back to a binary string.
# The solution also handles the case where the sum of two binary digits is greater 
# than 1 by adding a carry to the next digit.