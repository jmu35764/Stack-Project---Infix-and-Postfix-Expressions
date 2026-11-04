from stack import Stack
class PostfixEvaluator():
    def __init__(self, expression: str):
        self.expression = expression
        self.o_stack = Stack()
        self.result = 0

    def isOperator(self, char):
        if char in ('*', '+', '-', '/'):    
            return char

    def eval_postfix(self):
        for char in expression:
            if char is int:
                self.o_stack.push(char)

            elif isOperator(char):
                operands = [2]
                for i in range (1 to 3):
                    operands[i] = self.o_stack.pop()
                result = operands[1] char operands[2]

if __name__ == "__main__":

    test = InfixToPostfixConverter("53+")
    test.convert_to_postfix()




