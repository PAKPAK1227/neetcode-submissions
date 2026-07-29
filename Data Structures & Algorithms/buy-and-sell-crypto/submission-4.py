class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers left and right
        # calcualte max profit at each time
        # only move left if right is ever lower than current left
        # sliding window is
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
                continue
            curr_profit = prices[right] - prices[left]
            max_profit = max(curr_profit, max_profit)
            right += 1
            
        return max_profit