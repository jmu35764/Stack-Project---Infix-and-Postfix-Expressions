from stack import Stack
class InfixToPostfixConverter:
    def __init__(self, expression: str, stack:Stack):
        self.expression = expression
        self.stack = stack


    def isOperand(c):
        return 'A' <= c <= 'Z'

    def isOperator(c):
        if ord(c) == 42 or ord(c) == 43 or ord(c) == 45 or ord(c) == 47:
            return c


    def OpPrecedence(c):
        if ord(c) == 42 or ord(c) == 45:
            return 1
        else:
            return 2

    def convert_to_postfix(expression):
        for char in expression:
	        if isOperand(char):
		        result  += char

	        elif char isOperator(char):
		        while stack.is_empty() is False and OpPrecedence(stack.peak()) > 1:
			        stack.pop()
			        result += char
                stack.push(char)
	        
            elif char is '(':
		        stack.push(char)

	        elif char is ')':
		        while stack.peek() is not '(':
			        stack.pop()
		        stack.pop()
	        
            else:
		        ValueError("Invalid Operand")

        while stack.is_empty() is False:
            result += stack.pop()

        return result
            

if __name__ == "__main__":
    
    test = InfixToPostfixConverter("A+B*C")






