class WordDictionary:

    def __init__(self):
        self.graph = {}

    def addWord(self, word: str) -> None:
        curr = self.graph
        for i in range(len(word)):
            if word[i] not in curr:
                curr[word[i]] = [{}, False]
            if i == len(word) - 1:
                curr[word[i]][1] = True
            curr = curr[word[i]][0]

    def search(self, word: str) -> bool:
        def helper(currNode, lettersLeft):
            if not lettersLeft:
                return currNode[1]
            if lettersLeft[0] != '.':
                if lettersLeft[0] in currNode[0]:
                    return helper(currNode[0][lettersLeft[0]], lettersLeft[1:])
                else:
                    return False
            else:
                return any(helper(currNode[0][c], lettersLeft[1:]) for c in currNode[0])

        return helper([self.graph, False], word)