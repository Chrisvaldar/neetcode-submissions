from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for thing in strs:
            alpha = [0] * 26
            for char in thing:
                alpha[ord(char) - ord('a')] += 1
            words[tuple(alpha)].append(thing)
        
        return list(words.values())