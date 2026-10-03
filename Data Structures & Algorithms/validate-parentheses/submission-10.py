class Solution:
    def isValid(self, s: str) -> bool:
        # if you see a closing parenthesis, the parenthesis at the top of the stack must match
        # Must have an even number of parenthesis

        if len(s) % 2 != 0:
            return False
        parenthesis = {}

        parenthesis['}'] = '{'
        parenthesis[']'] = '['
        parenthesis[')'] = '('

        # openers = ['{', '[', '(']
        # closers = ['}', ']', ')']

        stack = []

        for i, p in enumerate(s):
            print(p)
            if p in parenthesis:
                if len(stack) == 0:
                    return False
                if stack.pop() != parenthesis[p]:
                    # print(s.pop)
                    # print(parenthesis[p])
                    return False
            else:
                stack.append(p)

        if len(stack) != 0:
            return False

        return True