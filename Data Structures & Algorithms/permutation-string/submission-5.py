class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # store s1 into an alphabetKey
        # abc = a[1]b[1]c[1] (The index is the character value in the alphabet)
        # store s2 the same way into a window
        # while window == len(alphabetKey)
            # if alphabetKey == window (that means that every index has the same value) so return True
            # otherwise window at the beginning of s2 gets removed

        alphabetKey = 26 * [0]

        for c in s1:
            alphabetKey[ord(c) - ord('a')] += 1
        
        window = 26 * [0]
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            window[ord(c) - ord('a')] += 1

            while (r - l + 1) == len(s1):
                if window == alphabetKey:
                    return True
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
        
        return False
