class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best,left,right = 0,0,0
        for i in range(len(prices) - 1, -1, -1):
            if prices[i] > right:
                right = prices[i]
                left = right
            elif prices[i]<left:
                left = prices[i]
                if best<right-left:
                    best = right-left

        return best
