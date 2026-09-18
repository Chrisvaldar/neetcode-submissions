from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        check = defaultdict(int)
        res = 0

        for right in range(len(s)):
            check[s[right]] += 1
            while right - left + 1 - max(check.values()) > k:
                check[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        
        return res
        
            