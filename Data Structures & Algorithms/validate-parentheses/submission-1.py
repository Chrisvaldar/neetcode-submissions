class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            
            try:
                if char == ")":
                    if stack.pop() != "(":
                        return False
                elif char == "}":
                    if stack.pop() != "{":
                        return False
                elif char == "]":
                    if stack.pop() != "[":
                        return False
            except:
                return False
        
        if stack:
            return False
        return True
        