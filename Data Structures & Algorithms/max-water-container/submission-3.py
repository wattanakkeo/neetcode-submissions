class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # while l < r
            # height = min(heights[l], heights[r])
            # res = max(res, (r - l) * height)
            # if heights[l] < heights[r]
                # l++
            # else
                # r--
        # return res

        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            height = min(heights[l], heights[r])
            res = max(res, (r - l) * height)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return res