class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #pre and post
        #[1,1,2,8] 
        #[48,24,6,1]
        #[1,-1,0,0,0]
        #[0,6,6,3,1]

        #loop through the arr and find the pre and store into map
        #key = index, value = pre

        #loop through the arr and find the post and store into map
        #key = index, value *= post

        #loop through the map and display

        n = len(nums)
        output = [1] * n

        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]
    
        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]

        return output
            



