class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        #set of all char
        #loop through the set to check which swap is better
            #reset the frequency and l window
            #loop r through entire list
                #while (windowLen - mostFreqChar > k)
                    #shift left pointer up
                #res = max(res, windowLen)

        # windowLen - mostFreqChar = replacements, compare replacements to k
        #windowLen == (r - l + 1), mostFreqChar = frequency

        res = 0
        characters = set(s)

        for c in characters:
            freq = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    freq += 1
                while ((r - l + 1) - freq) > k:
                    if s[l] == c:
                        freq -= 1
                    l += 1
                res = max(res, r - l + 1)
        
        return res
                