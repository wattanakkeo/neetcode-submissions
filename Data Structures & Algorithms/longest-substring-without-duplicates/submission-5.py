class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # create a set to store whats in the window
        # loop r through s
            # add into the set
            # while s[r] in set
                # remove s[l] from the set
                # l++
            # res = max(res, r - l + 1) which is windowLen
        # return res

        contiguous = set()
        l, res = 0, 0

        for r in range(len(s)):
            while s[r] in contiguous:
                contiguous.remove(s[l])
                l += 1
            
            contiguous.add(s[r])
            res = max(res, r - l + 1)
     
        return res