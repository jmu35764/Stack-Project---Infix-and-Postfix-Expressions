from stack import Stack
class InfixToPostfixConverter:
    def __init__(self, expression: str):
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
                if i != 0:
                    if self.isOperand(char) and self.isOperand(self.expression[i-1]):
                        raise ValueError("No two operators together")
                self.result  += char
                
            elif self.isOperator(char):

                if char == self.expression[0] or char == self.expression[-1]:
                    raise ValueError("Improper Placement of operator")
                elif self.isOperator(char) and self.isOperator(self.expression[i-1]):
                    raise ValueError("No two operators together")

                while not self.o_stack.is_empty() and \
                self.isOperator(self.o_stack.peek()) and \
                (self.OpPrecedence(self.o_stack.peek()) == 2 or self.OpPrecedence(self.o_stack.peek()) == self.OpPrecedence(char)):

                    
                    self.result += self.o_stack.pop()
                self.o_stack.push(char)

            elif char == '(':
                if ')' not in self.expression:
                    raise ValueError("No Matching Parantheses")
                self.o_stack.push(char)
                #print(self.o_stack._data)

            elif char == ')':
                if '(' not in self.o_stack._data:
                    raise ValueError("No matching Parantheses")
                for char in self.o_stack._data:
                    if self.o_stack.peek() != '(':
                        self.result += self.o_stack.pop()
                    if self.o_stack.peek() == '(':
                        self.o_stack.pop()

            else:
                raise ValueError("Invalid Operand");
            i += 1
                    
        while not self.o_stack.is_empty():
            self.result += self.o_stack.pop()

        return print(self.result)
            

if __name__ == "__main__":
    
    #s1 = Stack()
    test = InfixToPostfixConverter("A+B*C")
    test.convert_to_postfix()

    test_02 = InfixToPostfixConverter("(A+B)*C")
    test_02.convert_to_postfix()

    test_03 = InfixToPostfixConverter("A*B+C/D")
    test_03.convert_to_postfix()

    test_04 = InfixToPostfixConverter("(A+B)*(C-D)")
    test_04.convert_to_postfix()

    test_05 = InfixToPostfixConverter("A+B*C-D/E")
    test_05.convert_to_postfix()

    test_06 = InfixToPostfixConverter("A*(B+C)/D")
    test_06.convert_to_postfix()

    test_07 = InfixToPostfixConverter("(A+B*C)/(D-E)")
    test_07.convert_to_postfix()

    test_08 = InfixToPostfixConverter("A+(B-C)*D")
    test_08.convert_to_postfix()

    test_09 = InfixToPostfixConverter("(A+B*(C-D))/E")
    test_09.convert_to_postfix()

    test_10 = InfixToPostfixConverter("(A+B")
    test_10.convert_to_postfix()