from stack import Stack
class PostfixEvaluator():
    def __init__(self, expression):
        self.expression = expression
        self.o_stack = Stack()
        self.result = 0

    def isOperand(self, char):
        #print(char, "Operand",type(char))
        #if isinstance(char, float):
        if type(char) is int:
            return True

    def isOperator(self, char):
        #print(char, "Operator",type(char))
        if char in ('*', '+', '-', '/'):    
            return char

    def eval_postfix(self):
        #print(self.expression)
        operator_num = 0
        operand_num = 0
        for char in self.expression:
            #er_string = " "
            
            #print(type(char))
            if self.isOperand(char):
                operand_num += 1
                self.o_stack.push(char)
                
            elif self.isOperator(char):
                operator_num += 1
                operands = [0]*2
                if self.isOperand(self.expression[0]) and self.isOperator(self.expression[1]):
                    try:
                        raise ValueError("Can't have an operator after first operand")
                    except ValueError as e:
                        return print("[", *self.expression, "] -> ERROR: ",e)
                if self.o_stack.size() == 1:
                    try:
                        raise ValueError("Too many operators")
                    except ValueError as e:
                        return print("[", *self.expression, "] -> ERROR: ",e)
                for i in range (2):
                    operands[i] = self.o_stack.pop()
                #print(operands)
                if char == '+':
                    result = operands[1] + operands[0]
                    self.o_stack.push(result)
                if char == '-':
                    result = operands[1] - operands[0]
                    self.o_stack.push(result)
                if char == '*':
                    result = operands[1] * operands[0]
                    self.o_stack.push(result)
                if char == '/':
                    try:
                        if operands[0] == 0:
                            raise ZeroDivisionError("Can't divide by Zero")
                    except ZeroDivisionError as e:
                            return print("[", *self.expression, "] -> ERROR: ",e)
                            #result == 0
                            #break
                    else:
                        result = operands[1]/operands[0]
                        self.o_stack.push(result)
            
            else:
                try:
                    raise ValueError("Invalid Operand")
                except ValueError as e:
                    return print("[", *self.expression, "] -> ERROR: ",e)

        if self.o_stack.size() > 1:
            try:
                raise ValueError("Too many operands")
            except ValueError as e:
                return print("[", *self.expression, "] -> ERROR: ",e)
            
        return print("[", *self.expression, f"] = {self.o_stack.peek()}")



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
