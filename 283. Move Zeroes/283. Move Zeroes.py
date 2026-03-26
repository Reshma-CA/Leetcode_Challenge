from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = []
        non_zero = []
        for item in nums:
            if item == 0:
                zeros.append(item)
            else:
                non_zero.append(item)

        result = non_zero+zeros
        nums[:] = result

        