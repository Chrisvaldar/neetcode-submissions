class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # def isAnagram(s: str, t: str) -> bool:
        #     if len(s) != len(t):
        #         return False

        #     countS, countT = {}, {}

        #     for i in range(len(s)):
        #         countS[s[i]] = 1 + countS.get(s[i], 0)
        #         countT[t[i]] = 1 + countT.get(t[i], 0)
        #     return countS == countT

        # seen = []
        # res = []
        # for i in range(len(strs)):
        #     if strs[i] not in seen:
        #         group = [strs[i]]
        #         seen.append(strs[i])
        #         for j in range (i+1, len(strs)):
        #             if isAnagram(strs[i], strs[j]):
        #                 group.append(strs[j])
        #                 seen.append(strs[j])
        #         res.append(group)
        
        # return res
        res = []
        anagrams = {}
        for thing in strs:
            temp = thing
            thing = "".join(sorted(thing))
            if thing not in anagrams:
                anagrams[thing] = [temp]
            else:
                anagrams[thing].append(temp)
        
        for value in anagrams.values():
            res.append(value)
        return res


                