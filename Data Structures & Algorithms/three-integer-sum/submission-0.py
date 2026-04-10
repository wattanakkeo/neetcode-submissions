class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #[-4, -1, -1, 0, 1, 2]

        for i, a in enumerate(nums):
            if (a > 0):
                break
            if (i > 0 and a == nums[i - 1]):
                continue
            
            l = i + 1;
            r = len(nums) - 1
            while (l < r):
                threeSum = nums[l] + nums[r] + a
                if (threeSum < 0):
                    l += 1
                elif (threeSum > 0):
                    r -= 1
                else:
                    res.append([nums[l], nums[r], a])
                    l += 1
                    r -= 1
                    while (l < r and nums[l] == nums[l - 1]):
                        l += 1
        return res