from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        check1 = defaultdict(int)
        check2 = defaultdict(int)
        left = 0
        right = len(s1) -1

        for char in s1:
            check1[char] += 1

        for i in range(left,right + 1):
            check2[s2[i]] += 1

        while right < len(s2):
            if check1 == check2:
                return True
            else:
                check2[s2[left]] -= 1
                if check2[s2[left]] == 0:
                        del check2[s2[left]]
                left += 1
                right += 1
                if right < len(s2):
                    check2[s2[right]] += 1
        return False
