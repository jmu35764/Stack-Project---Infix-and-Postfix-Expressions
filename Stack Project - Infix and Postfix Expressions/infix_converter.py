from stack import Stack
class InfixToPostfixConverter:
    def __init__(self, expression):
        self.expression = expression
        self.o_stack = Stack()
        self.result = ""


    def isOperand(self, char):
        if 'A' <= char <= 'Z':
            return char

    def isOperator(self, char):
        if char in ('*', '+', '-', '/'):    
            return char


    def OpPrecedence(self, char):
        if ord(char) == 43 or ord(char) == 45:
            return 1
        else:
            return 2

    def convert_to_postfix(self):
        #print("Code is running")
        i = 0
        for char in self.expression:
            
            if self.isOperand(char):
                try:
                    if i != 0:
                        if self.isOperand(char) and self.isOperand(self.expression[i-1]):
                            raise ValueError("No Operator between operands")
                except ValueError as e:
                    return print("[", *self.expression, "] -> ERROR: ",e)
                    #while not self.o_stack.is_empty():
                    #    self.o_stack.pop()
                    #self.result = ""
                    #break

                else:
                    self.result  += char
                
            elif self.isOperator(char):

                try:
                    if char == self.expression[0] or char == self.expression[-1]:
                        raise ValueError("Improper Placement of operator")
                    elif self.isOperator(char) and self.isOperator(self.expression[i-1]):
                        raise ValueError("No two operators together")
                except ValueError as e:
                    return print("[", *self.expression, "] -> ERROR: ",e)
                    #if not self.o_stack.is_empty():
                    #    self.o_stack.pop()
                    #self.result = ""
                    #break

                else:
                    while not self.o_stack.is_empty() and \
                    self.isOperator(self.o_stack.peek()) and \
                    (self.OpPrecedence(self.o_stack.peek()) == 2 or self.OpPrecedence(self.o_stack.peek()) == self.OpPrecedence(char)):

                    
                        self.result += self.o_stack.pop()
                    self.o_stack.push(char)

            elif char == '(':
                try:
                    if ')' not in self.expression:
                        raise ValueError("Parantheses Don't Match")
                except ValueError as e:
                    while not self.o_stack.is_empty():
                        self.o_stack.pop()
                    return print("[", *self.expression, "] -> ERROR: ",e)
                    #self.result = ""
                    #break
                else:
                    self.o_stack.push(char)
                #print(self.o_stack._data)

            elif char == ')':
                try:
                    if '(' not in self.o_stack._data:
                        raise ValueError("Parantheses don't match")
                except ValueError as e:
                    while not self.o_stack.is_empty():
                        self.o_stack.pop()
                    return print("[", *self.expression, "] -> ERROR: ",e)
                    #self.result = ""
                    #break
                else:
                    for char in self.o_stack._data:
                        if self.o_stack.peek() != '(':
                            self.result += self.o_stack.pop()
                        if self.o_stack.peek() == '(':
                            self.o_stack.pop()

            else:
                try:
                    raise ValueError("Invalid Operand")
                except ValueError as e:
                    return print("[", *self.expression, "] -> ERROR: ",e)
                    #self.result = ""
                    #break
            i += 1
                    
        while not self.o_stack.is_empty():
            self.result += self.o_stack.pop()

        return print(self.result)
            

if __name__ == "__main__":
    
    #s1 = Stack()
    test = InfixToPostfixConverter(['A','+','B','*','C'])
    test.convert_to_postfix()

    test_02 = InfixToPostfixConverter(['(','A','+','B',')','*','C'])
    test_02.convert_to_postfix()

    test_03 = InfixToPostfixConverter(['A','*','B','+','C','/','D'])
    test_03.convert_to_postfix()

    test_04 = InfixToPostfixConverter(['(','A','+','B',')','*','(','C','-','D',')'])
    test_04.convert_to_postfix()

    test_05 = InfixToPostfixConverter(['A','+','B','*','C','-','D','/', 'E'])
    test_05.convert_to_postfix()

    test_06 = InfixToPostfixConverter(['A','*','(','B','+','C',')','/','D'])
    test_06.convert_to_postfix()

    test_07 = InfixToPostfixConverter(['(','A','+','B','*','C',')','/','(','D','-','E',')'])
    test_07.convert_to_postfix()

    test_08 = InfixToPostfixConverter(['A','+','(','B','-','C',')','*','D'])
    test_08.convert_to_postfix()

    test_09 = InfixToPostfixConverter(['(','A','+','B','*','(','C','-','D',')',')','/','E'])
    test_09.convert_to_postfix()

    test_10 = InfixToPostfixConverter(['A','+','B',')','C'])
    test_10.convert_to_postfix()

    test_11 = InfixToPostfixConverter(['A','+','B',';','C'])
    test_11.convert_to_postfix()
    
    test_12 = InfixToPostfixConverter(['+','A','B'])
    test_12.convert_to_postfix()

    test_13 = InfixToPostfixConverter(['A','+','*','B'])
    test_13.convert_to_postfix()

    test_14 = InfixToPostfixConverter(['A','B','+','C'])
    test_14.convert_to_postfix()

    test_15 = InfixToPostfixConverter(['A','+',')','B','*','C'])
    test_15.convert_to_postfix()
    
    test_16 = InfixToPostfixConverter(['(','A','+','B'])
    test_16.convert_to_postfix()

    test_17 = InfixToPostfixConverter(['A','+','B',')'])
    test_17.convert_to_postfix()