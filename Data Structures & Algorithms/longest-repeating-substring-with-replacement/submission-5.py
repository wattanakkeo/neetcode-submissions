class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # create a window map to track whats in the window
        # loop r through s
            # add s[r] into map
            # mostFreq = max(mostFreq, window[s[r]])

            # while (r - l + 1 - mostFreq) > k
                # window[s[l]] -= 1
                # l++

            # res = max(res, r - l + 1)

        window = {}
        mostFreq = 0
        res = 0
        l = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            mostFreq = max(mostFreq, window[s[r]])

            while (r - l + 1 - mostFreq) > k:
                window[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        
        return res
        

