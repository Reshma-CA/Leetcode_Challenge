from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

          # Check every pair
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return -1
    
# we can use hashmap

def two_sum(nums, target):
# Use a dictionary to store number -> index mapping
    num_to_index = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    return []  # return empty if no solution found


# Example usage
res = two_sum([2, 7, 11, 15], 9)
print("Output:", res)
