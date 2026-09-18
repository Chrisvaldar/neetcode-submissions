class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        check = {}
        for thing in s:
            if thing in check:
                check[thing] += 1
            else:
                check[thing] = 1
            
        for thing in t:
            if thing in check:
                check[thing] -= 1
            else:
                return False

        for item in check.values():
            if item != 0:
                return False
        return True
        