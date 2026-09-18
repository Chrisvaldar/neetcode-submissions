class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left, right = 0, 0
        # maxLen = 0
        # while right < len(s):
        #     while s[right] in s[left:right]:
        #         left += 1
        #     else:
        #         maxLen = max(maxLen, right-left + 1)
        #     right += 1
        # return maxLen

        check = {}
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in check:
                left = max(check[s[right]] + 1, left)
            check[s[right]] = right
            res = max(res, right - left + 1)
        return res
