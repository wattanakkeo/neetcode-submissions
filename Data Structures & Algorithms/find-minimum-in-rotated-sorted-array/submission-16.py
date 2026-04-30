class Solution:
    def findMin(self, nums: List[int]) -> int:
        #nums=[4,5,6,7,,, 0,1,2] 
        #l =4, r =6, mid =5 res =1

        l, r = 0, len(nums) - 1
        res = nums[0]

        while (l <= r):
            if (nums[l] <= nums[r]):
                res = min(nums[l], res)
                break

            mid = (l + r) // 2 
            res = min(res, nums[mid])
            if (nums[mid] >= nums[l]):
                l = mid + 1
            else:
                r = mid - 1

        return res
        