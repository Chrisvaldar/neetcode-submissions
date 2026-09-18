class PrefixTree:

    def __init__(self):
        self.graph = {} #letter -> [{children}, isEnd]

    def insert(self, word: str) -> None:
        curr = self.graph
        for letter in word:
            if letter not in curr:
                curr[letter] = [{}, False]
            if letter == word[-1]:
                curr[letter][1] = True
            curr = curr[letter][0]

    def search(self, word: str) -> bool:
        curr = self.graph
        last = False
        for letter in word:
            if letter not in curr:
                return False
            if letter == word[-1] and curr[letter][1]:
                last = True
            curr = curr[letter][0]
        return last

    def startsWith(self, prefix: str) -> bool:
        curr = self.graph
        for letter in prefix:
            if letter not in curr:
                return False
            curr = curr[letter][0]
        return True
        
        