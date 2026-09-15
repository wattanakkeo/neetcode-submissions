class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #turn s1 into target code
        #loop r through s2
            #start adding into alphabetCode
            #if (r - l + 1) == windowLen
                #if target == alphabetCode return true
                #dec alphabetCode at index l
                #l++
        #return false

        target = [0] * 26 
        for c in s1:
            target[ord(c) - ord('a')] += 1

        l = 0
        windowLen = len(s1)
        alphabetCode = [0] * 26

        for r in range(len(s2)):
            alphabetCode[ord(s2[r]) - ord('a')] += 1
            if (r - l + 1) == windowLen:
                if alphabetCode == target:
                    return True
                alphabetCode[ord(s2[l]) - ord('a')] -= 1
                l += 1
        return False

