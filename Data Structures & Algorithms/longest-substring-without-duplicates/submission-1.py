class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #sliding window, set for duplicates
        #LOOP through substr
        #WHILE R in set, remove set at L
            #inc L
        #add R into set
        #inc R

        L = 0
        longest = 0
        nondupe = set()

        for R in range(len(s)):
            while s[R] in nondupe:
                nondupe.remove(s[L])
                L = L + 1
            nondupe.add(s[R])
            longest = max(longest, (R - L) + 1)
        
        return longest