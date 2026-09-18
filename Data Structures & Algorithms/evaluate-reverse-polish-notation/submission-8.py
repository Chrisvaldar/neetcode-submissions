class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        
        for char in tokens:
            try:
                stack.append(int(char))
            except:
                d1 = int(stack.pop())
                d2 = int(stack.pop())
                if char == '+':
                    res = d2 + d1 
                elif char == '-':
                    res = d2 - d1
                elif char == '*':
                    res = d2 * d1
                elif char == '/':
                    res = d2 / d1
                stack.append(res)
            print(stack)
        return int(stack[-1])
