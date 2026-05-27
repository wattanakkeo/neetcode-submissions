class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #WINDOW CONDITION: While there are no duplicates keep going

        numSet = set()
        l, r, maxSubstr, count = 0, 0, 0, 0

        for r in range(len(s)):
            while (s[r] in numSet):
                numSet.discard(s[l])
                l += 1
                count -= 1
            numSet.add(s[r])
            count += 1
            maxSubstr = max(count, maxSubstr)
        
        return maxSubstr
        