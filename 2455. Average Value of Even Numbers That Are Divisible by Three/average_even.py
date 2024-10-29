class Solution:
    def averageValue(self, nums: List[int]) -> int:
        total_sum = 0
        count = 0

        for i in nums:
            # Check if the number is both even and divisible by 3
            if i % 3 == 0 and i % 2 == 0:
                total_sum += i
                count += 1

        # Calculate the average if there are qualifying numbers
        if count > 0:
            average = total_sum // count  # Use integer division for rounding down
        else:
            average = 0  # Return 0 if no numbers qualify

        return average