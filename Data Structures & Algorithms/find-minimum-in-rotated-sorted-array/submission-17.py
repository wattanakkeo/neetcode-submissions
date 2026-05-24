class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #init least = nums[0]
    #Find our return value

            #if (nums[l] <= nums[r])
                #least = min(least, nums[l])

            # least = min(nums at mid, least)
        
    #Find our mid condition

            #if nums at mid > nums at left 
                # left = mid + 1
            #else right = mid - 1

        l, r = 0, len(nums) - 1
        least = nums[l]

        while (l <= r):
            if (nums[l] <= nums[r]):
                least = min(least, nums[l])
                break
        
            mid = (l + r) // 2

            least = min(nums[mid], least)
            if (nums[mid] >= nums[l]):
                l = mid + 1
            else:
                r = mid - 1
        
        return least