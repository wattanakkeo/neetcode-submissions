class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # init a list of size 26 for every char in alphabet
        # for loop through s1 to append values into alphabetCodeTarget
        # loop through s2
            # add to alphabetCodeStored
            # if stored == target return true
            # while the windowLen > len(s1)
                # alphabetCodeTarget[l] -= 1
                # l += 1
        # return false which means that within the loop we couldn't find a permutation

        alphabetCodeTarget = [0] * 26

        for c in s1:
            alphabetCodeTarget[ord(c) - ord('a')] += 1
        
        alphabetCodeStored = [0] * 26
        substrLen = len(s1)
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            alphabetCodeStored[ord(c) - ord('a')] += 1
            
            if (r - l + 1) == substrLen:
                if alphabetCodeStored == alphabetCodeTarget:
                    return True
                alphabetCodeStored[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False





            