class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right = 0, 0
        maxLen = 0
        while right < len(s):
            while s[right] in s[left:right]:
                left += 1
            else:
                maxLen = max(maxLen, right-left + 1)
            right += 1
        return maxLen