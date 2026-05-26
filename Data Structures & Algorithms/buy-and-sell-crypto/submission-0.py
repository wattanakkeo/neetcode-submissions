class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #WHAT MAKES THE WINDOW CONDITON VALID/TRUE
        #The window can only be of size (r - l) = 1
        
        #loop through nums
            #if (r - l) == 1:
                #maxProfit = the max of l - r
                #shift l + 1
        #return max profit

        l, maxProfit = 0, 0

        for r in range(1, len(prices)):
            if (prices[r] > prices[l]):
                maxProfit = max(maxProfit, (prices[r] - prices[l]))
            else:
                l = r
                
        return maxProfit
        