class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #use a hashmap key = alphabet code, value = str
        #where alphabet code is the ascii value sum of all the letters in the word
        # {alphabetCode: [pots, tops]}
        
        anagrams = dict()

        for word in strs:
            alphabetCode = [0] * 26

            for letter in word:
                alphabetCode[ord(letter) - ord("a")] += 1
            anagrams[tuple(alphabetCode)] = anagrams.get(tuple(alphabetCode), []) + [word]
        
        anagramsList = []

        for key in anagrams:
            anagramsList.append(anagrams[key])
        return anagramsList
