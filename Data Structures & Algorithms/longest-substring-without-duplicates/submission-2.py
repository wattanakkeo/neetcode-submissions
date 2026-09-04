class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #set to track if already in window
        #loop r in range len(s)
        #while s[r] in set remove s[l] and inc 
        #add s[r] in set
        #res = max(res, r - l + 1), windowLength = r - l + 1

        nonDupe = set()
        res = l = 0

        for r in range(len(s)):
            while s[r] in nonDupe:
                nonDupe.remove(s[l])
                l += 1
            nonDupe.add(s[r])
            res = max(res, r - l + 1)
        return res