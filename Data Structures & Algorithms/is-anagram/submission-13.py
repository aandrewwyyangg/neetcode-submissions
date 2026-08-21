from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        brute force:
        anagram means all chars rearrange to diff word so diff len = not anagram
        sorted makes order the same 
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
        '''
        
        count = {}

        if len(s) != len(t):
            return False

        return Counter(s) == Counter(t)