class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            while s[right] in curr:
                curr.remove(s[left])
                left += 1
            curr.add(s[right])
            longest = max(longest, right - left + 1)

        return longest