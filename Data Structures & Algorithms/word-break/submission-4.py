class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        reachable = {-1}
        wordDict = set(wordDict)
        
        for i in range(len(s)):
            for r in list(reachable):
                currString = s[r + 1:i + 1]
                if currString in wordDict:
                    reachable.add(i)
                
        return (len(s) - 1) in reachable
            
            