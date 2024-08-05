class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in matches.keys():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                comp = stack.pop()
                if matches[comp] != char:
                    return False
        return len(stack) == 0     
        
        