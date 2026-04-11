class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxHeight = 0

        #calculate current max height min of two * r (width)
        #if height of l < r shift l right
        #elif height of r < l shift r left
        #elif heights are equal
            #if l + 1 > r - 1 shift l right
            #else shift r left
        
        while (l < r):
            temp = min(heights[l], heights[r]) * (r - l)
            if (maxHeight < temp):
                maxHeight = temp

            if (heights[l] < heights[r]):
                l += 1
            elif (heights[r] < heights[l]):
                r -= 1
            elif (heights[l + 1] < heights[r - 1]):
                r -= 1
            else:
                l += 1
        
        return maxHeight
