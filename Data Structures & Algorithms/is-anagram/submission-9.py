class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagramCheck = {}

        if len(s) != len(t):
            return False

        for char in s: 
            anagramCheck[char] = anagramCheck.get(char, 0) + 1
        
        for char in t:
            anagramCheck[char] = anagramCheck.get(char, 0) - 1
        
        return all(value == 0 for value in anagramCheck.values())