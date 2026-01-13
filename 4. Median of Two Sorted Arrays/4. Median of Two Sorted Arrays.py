from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        
        n = len(merged)
        mid = n // 2
        
        # Step 2: Check if length is odd or even
        if n % 2 == 0:
            # Even length → average of middle two numbers
            return (merged[mid - 1] + merged[mid]) / 2
        else:
            # Odd length → middle number
            return merged[mid]


        