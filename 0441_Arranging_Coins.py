class Solution:
    def arrangeCoins(self, n: int) -> int:
        def search(lo, hi):
            i = (lo + hi) // 2
            left = i * (i + 1) // 2
            right = (i + 1) * (i + 2) // 2
            
            if left <= n < right:
                print(i)
                return i
            
            elif n < left: 
                return search(lo, i)
            else:
                return search(i, hi)

        return search(1, n)

# This solution runs in O(log n) time complexity where n is the input integer representing the number of coins. This is 
# because it uses a binary search approach to find the maximum number of complete rows that can be formed with the given
# coins. The search space is halved in each recursive call, leading to a logarithmic time complexity. The space complexity
# is O(1) since it uses tail recursion without any additional data structures that grow with input size.