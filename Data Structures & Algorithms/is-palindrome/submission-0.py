class Solution:
    def isPalindrome(self, s: str) -> bool:
        ##ascii values A-Z, a-z 65-90, 97-122
        ##0-9 48-57

        #turn everything into lower
        #skip all non-alphanumeric

        #check left and right if theyre even until they cross paths

        validChar = ''

        for letter in s:
            if (letter >= 'A' and letter <= 'Z'
                or letter >= 'a' and letter <= 'z'
                or letter >= '0' and letter <= '9'):
                letter = letter.lower()
                validChar += letter
        
        left = 0
        right = len(validChar) - 1

        while (left < right):
            if (validChar[left] != validChar[right]):
                return False
            left += 1
            right -= 1
        return True
        
