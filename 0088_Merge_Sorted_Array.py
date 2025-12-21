from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        del nums1[m::]
        iter_1 = 0
        iter_2 = 0

        while len(nums1) != m + n:
            if(iter_1 >= len(nums1)):
                while(iter_2 < n):
                    nums1.append(nums2[iter_2])
                    iter_2 += 1
                break
            if(nums2[iter_2] < nums1[iter_1]):
                nums1.insert(iter_1, nums2[iter_2])
                iter_2 += 1
            iter_1 += 1
