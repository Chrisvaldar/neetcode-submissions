class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(open_used, closed_used):
            if open_used == closed_used == n:
                res.append("".join(stack))
            
            if open_used < n:
                stack.append("(")
                backtrack(open_used + 1, closed_used)
                stack.pop()
            if closed_used < open_used:
                stack.append(")")
                backtrack(open_used, closed_used + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res
