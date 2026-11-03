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
        for char in self.expression:
            #print(self.o_stack._data)
            if self.isOperand(char):
                self.result  += char
                
            elif self.isOperator(char):
                while not self.o_stack.is_empty() and self.isOperator(self.o_stack.peek()) and (self.OpPrecedence(self.o_stack.peek()) == 2 or self.OpPrecedence(self.o_stack.peek()) == self.OpPrecedence(char)):
                    #print("The Precedence of the current stack item is: ", self.OpPrecedence(char))
                    self.result += self.o_stack.pop()
                self.o_stack.push(char)

            elif char == '(':
                self.o_stack.push(char)
                #print(self.o_stack._data)

            elif char == ')':
                #while self.o_stack.peek != '(':
                    #print(self.o_stack._data)
                    #self.result += self.o_stack.pop()

                for char in self.o_stack._data:
                    if self.o_stack.peek() != '(':
                        self.result += self.o_stack.pop()
                    if self.o_stack.peek() == '(':
                        self.o_stack.pop()
                    
                #self.o_stack.pop()

            #print("Current result is: ", self.result)
        
        #print(self.o_stack._data)
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