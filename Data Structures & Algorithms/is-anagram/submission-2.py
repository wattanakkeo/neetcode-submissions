class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #create a map to store each letter
        #loop through to check if the other str contains each letter

        characters = {}

        for char in s:
            characters[char] = characters.get(char, 0) + 1
        
        for char in t:
            characters[char] = characters.get(char, 0) - 1

        for count in characters.values():
            if count != 0:
                return False
        return True