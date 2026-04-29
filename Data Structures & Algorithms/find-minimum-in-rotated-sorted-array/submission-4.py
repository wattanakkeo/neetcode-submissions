class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 3 ,4 , 5 , 6 , 1 , 2
        # l = 3, mid = 5, r = 2
        #0         2         5

        # 4, 5, 6, 1, 2, 3
        # l = 4 , mid = 6, r = 3

        # 5, 6, 1, 2 ,3 ,4
        # l = 5 , mid = 1, r = 4

        # 6, 1, 2, 3, 4, 5
        # l = 6 , mid = 2, r = 5

        l, r = 0, len(nums) - 1
        res = nums[0]

        while (l <= r):
            if (nums[l] < nums[r]):
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(nums[mid], res)
            if (nums[mid] >= nums[l]):
                l = mid + 1
            else:
                r = mid - 1
            
            
        return res



        