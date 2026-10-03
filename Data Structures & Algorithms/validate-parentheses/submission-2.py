class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False
        
        # Create a brackets dictionary to match the closing and opening braces
        closingBrackets = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for i in s:
            if i in closingBrackets:
                if not stack:
                    return False
                if stack[-1] != closingBrackets[i]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(i)
    
        return True if not stack else False