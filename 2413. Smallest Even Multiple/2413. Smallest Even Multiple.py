class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n%2 ==0:
            return n

        if n%2 ==1:
            return n*2