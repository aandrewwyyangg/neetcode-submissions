from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force: sort every word, count each letter return list of lists of each word that is sorted the same? 

        count = {}
        
        for word in strs:
            key = "".join(sorted(word))
            if key not in count:
                count[key] = [word]
            else:
                count[key].append(word)

        return list(count.values())
        