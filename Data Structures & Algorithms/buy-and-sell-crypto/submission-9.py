class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left pointer starts at day 0 
        # right pointer starts at day 1 
        # left pointer represents buying, right pointer is selling
        # if left is greater than right, update both left and right to the next day 
        # compare max profits and update accordingly
        # if left is less than right, just move right, since that's still the lowest purchase so far
        
        left = 0
        right = 1 
        max_profit = 0

        while right < len(prices): 
            # profitable?
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
            right += 1
        return max_profit