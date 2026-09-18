from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Dict shape: (type of group, num of group) -> set
        # Example: (r, 1) -> {1,2,3} means the row 1 (0 indexed) has numbers 1, 2, 3
        # To calculate box, we can use //3 on both r and c and have that be our index for a box
        # i.e. (b, (r//3, c//3))

        count = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[i])):
                curr = board[i][j]
                if curr == '.':
                    continue
                rowTup = ("r", i)
                colTup = ("c", j)
                boxTup = ("b", (i // 3, j // 3))

                if curr in count[rowTup] or curr in count[colTup] or curr in count[boxTup]:
                    return False

                count[rowTup].add(curr)
                count[colTup].add(curr)
                count[boxTup].add(curr)

        
        return True