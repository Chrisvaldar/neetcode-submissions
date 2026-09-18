from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        check = defaultdict(int)
        res = 0
        
        for right in range(len(s)):
            check[s[right]] += 1
            while right - left + 1 - max(check.values()) > k:
                check[s[left]] -= 1
                left += 1
            res = max(res, right - left + 1)
        return res
        # while right < len(s):
        #     while s[right] != s[left] and k > 0:
        #         if k > 0:
        #             k -= 1
        #             break
        #         else:
        #             left += 1
        #     res = max(res, right-left + 1)
        #     right += 1
        
        # return res


