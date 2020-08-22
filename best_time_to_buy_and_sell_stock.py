from typing import List
import sys

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # #Method1. 이중for문
        # max_diff = 0
        # for start in range(len(prices)-1):
        #     for end in range(start+1, len(prices)):
        #         if prices[end]-prices[start] > max_diff:
        #             max_diff = prices[end]-prices[start]
        
        # return max_diff

        #Method2. 최댓값, 최솟값 갱신
        profit = 0
        min_price = sys.maxsize #None으로 선언하면 비교시 타입에러 발생

        #최댓값과 최솟값을 입력에 따라 갱신한다
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)

        return profit
            
            

            