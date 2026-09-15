class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqueChar = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in uniqueChar:
                uniqueChar.remove(s[l])
                l += 1
            uniqueChar.add(s[r])
            res = max(res, r - l + 1)

        
        return res 