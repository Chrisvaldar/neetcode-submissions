class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[0], 0)]
        res = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            curr = temperatures[i]
            check_val, check_idx = stack[-1]
            while stack and curr > check_val:
                stack.pop()
                res[check_idx] = i - check_idx
                if stack:
                    check_val, check_idx = stack[-1]
            stack.append((curr, i))
        return res
            


        