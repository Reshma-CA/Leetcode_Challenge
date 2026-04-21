class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = float('inf')
        max_profit = 0

        for item in prices:
            if item < min_price:
                min_price = item

            profit = item - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit