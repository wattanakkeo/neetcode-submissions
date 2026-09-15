class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0

        for r in range(len(prices)):
            while prices[l] > prices[r]:
                l += 1
            if prices[l] < prices[r]:
                res = max(res, prices[r] - prices[l])
        return res
