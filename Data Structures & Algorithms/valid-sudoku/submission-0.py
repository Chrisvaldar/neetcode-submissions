class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == ".":
                    continue

                row_thing = ("r", curr, i)
                coll_thing = ("c", curr, j)
                box_thing = ("box", curr, i//3, j//3)
        
                if row_thing in seen or coll_thing in seen or box_thing in seen:
                    return False
                seen.add(row_thing)
                seen.add(coll_thing)
                seen.add(box_thing)
        return True