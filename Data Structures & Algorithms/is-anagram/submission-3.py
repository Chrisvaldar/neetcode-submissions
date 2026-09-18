from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = defaultdict(int)
        hash_t = defaultdict(int)
        for i in s:
            hash_s[i] += 1

        for j in t:
            hash_t[j] += 1

        return hash_s == hash_t