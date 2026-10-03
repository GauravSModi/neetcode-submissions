class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        operators = ['+', '-', '*', '/']

        # Edge cases:
        # Empty list
        # Incorrect number of operations to numbers?
        # Add numbers to stack. When you see an operation, pull the last two numbers from the stack
        
        for token in tokens:
            if token in operators:
                operand2 = numstack.pop()
                operand1 = numstack.pop()
                print(operand1, operand2)
                match token:
                    case '+':
                        numstack.append(operand1 + operand2)
                    case '-':
                        numstack.append(operand1 - operand2)
                    case '*':
                        numstack.append(operand1 * operand2)
                    case '/':
                        if operand2 == 0:
                            numstack.append(0)
                        else:
                            result = int(operand1 / operand2)
                            numstack.append(result)
            else:
                numstack.append(int(token))

        return numstack.pop()
