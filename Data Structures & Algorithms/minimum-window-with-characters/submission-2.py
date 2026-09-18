from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        check_t = defaultdict(int)
        check_s = defaultdict(int)

        for i in range(len(t)):
            check_t[t[i]] += 1

        left = 0
        right = 0
        need = len(check_t)
        have = 0
        minString = None
        while right < len(s):
            
            if s[right] in check_t.keys():
                check_s[s[right]] += 1
                if check_s[s[right]] == check_t[s[right]]:
                    have += 1
            right += 1
                
            while have == need:
                if minString is None or len(s[left:right]) < len(minString):
                    minString = s[left:right]
                if s[left] in check_t and check_s[s[left]] == check_t[s[left]]:
                    have -= 1
                check_s[s[left]] -= 1
                left += 1

        return minString or ""
        
        
