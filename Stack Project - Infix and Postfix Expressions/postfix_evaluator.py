from stack import Stack
class PostfixEvaluator():
    def __init__(self, expression):
        self.expression = expression
        self.o_stack = Stack()
        self.result = 0

    def isOperand(self, char):
        if isinstance(char, int):
            return char

    def isOperator(self, char):
        if char in ('*', '+', '-', '/'):    
            return char

    def eval_postfix(self):
        for char in self.expression:
            
            if self.isOperand(char):
                self.o_stack.push(char)
                

            elif self.isOperator(char):
                operands = [0]*2
                for i in range (2):
                    operands[i] = self.o_stack.pop()
                if char == '+':
                    result = operands[1] + operands[0]
                if char == '-':
                    result = operands[1] - operands[0]
                if char == '*':
                    result = operands[1] * operands[0]
                if char == '/':
                    result = operands[1] / operands[0]
                self.o_stack.push(result)
            else:
                raise ValueError("Invalid Operand");
        return print(self.o_stack.peek())

if __name__ == "__main__":

    test_00 = PostfixEvaluator([5, 3,'+'])
    test_00.eval_postfix()

    test_01 = PostfixEvaluator([8, 2,'-', 3,'+'])
    test_01.eval_postfix()

    test_02 = PostfixEvaluator([5, 3, 8,'*','+'])
    test_02.eval_postfix()

    test_03 = PostfixEvaluator([5, 3, 8,'*','+', 2,'/'])
    test_03.eval_postfix()

    test_04 = PostfixEvaluator([5, 3,'+', 8, 2,'/','-'])
    test_04.eval_postfix()

    test_05 = PostfixEvaluator([35, 27,'+', 3, '*'])
    test_05.eval_postfix()
