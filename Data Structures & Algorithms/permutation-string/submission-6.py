class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # OPTIMAL: O(n)
        # sliding window, and store s1 into an alphabetKey
        # build the window in the for loop and while amount of char are equal start checking equality

        alphabetKey = [0] * 26
        for c in s1:
            alphabetKey[ord(c) - ord('a')] += 1

        l = 0
        window = [0] * 26

        for r in range(len(s2)):
            c = s2[r]
            window[ord(c) - ord('a')] += 1

            if ((r - l + 1) == len(s1)):
                if window == alphabetKey:
                    return True
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False
