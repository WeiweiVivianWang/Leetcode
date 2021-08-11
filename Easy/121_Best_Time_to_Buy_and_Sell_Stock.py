class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = sys.maxsize
        max_price = 0
#对于每一天的价格，我考虑在那天之前的最低价买入，看看是不是能跟新答案。       
        for i in prices:
            if i - min_price > max_profit:
                max_profit = i - min_price
                
            if i < min_price:
                min_price = i
                
        return max_profit
        