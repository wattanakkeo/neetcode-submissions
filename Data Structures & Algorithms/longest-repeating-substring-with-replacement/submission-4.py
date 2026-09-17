class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = {}
        mostFreq = 0
        res = 0
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            mostFreq = max(mostFreq, window[c])

            while (r - l + 1 - mostFreq) > k:
                window[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)
        return res