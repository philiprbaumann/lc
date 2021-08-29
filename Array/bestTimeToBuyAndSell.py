#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution(object):
    def maxProfit(self, prices):
        min = prices[0]
        earnings = 0
        for price in prices:
            if price > min and price-min > earnings:
                earnings = price - min
            elif price < min:
                min = price 
        return earnings
        """
        :type prices: List[int]
        :rtype: int
        """