# method=>1

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
       return nums+nums

# method=>2

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

       for i in range(len(nums)):
           nums.append(nums[i])
       return nums


# method=>3
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       return nums*2

# method=>4
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
       nums.extend(nums)
       return nums