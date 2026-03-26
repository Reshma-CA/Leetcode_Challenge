from typing import List
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n*(n+1)//2
        sum_of_array = sum(nums)
        result = expected_sum - sum_of_array
        return result

    
           