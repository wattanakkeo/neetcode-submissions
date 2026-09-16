class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #loop r through len(list)
            #calculate sum of window
            #while sum == target
                #calculate the window length
                #save the min
                #shrink the window
                #subtract l

        l, total = 0, 0
        res = float("infinity")

        for r in range(len(nums)):
            total += nums[r]
        
            while total >= target:
                res = min(res, r - l + 1)
                total -= nums[l]
                l += 1
        return res if res != float("infinity") else 0

        target=7
        nums=[2,3,1,2,4,3]