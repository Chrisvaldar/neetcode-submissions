from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for string in strs:
            freq = [0] *  26
            for char in string:
                freq[ord(char) - ord('a')] += 1
            anagrams[tuple(freq)].append(string)

        return [anagrams[x] for x in anagrams]

