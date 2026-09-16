class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            alphabetCode = [0] * 26

            for c in word:
                alphabetCode[ord(c) - ord('a')] += 1
            anagrams[tuple(alphabetCode)] = anagrams.get(tuple(alphabetCode), []) + [word]
        
        res = []
        for k in anagrams:
            res.append(anagrams[k])

        return res