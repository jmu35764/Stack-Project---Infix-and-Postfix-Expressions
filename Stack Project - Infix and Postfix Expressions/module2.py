from stack import Stack
from infix_converter import InfixToPostfixConverter
class I_P_Error(Exception):
    "Rasied when there is an error in the math line"
    #pass
    def __init__(self, char, expression):
        self.char = char
        self.expression = expression
        #self.stack = stack

    def adjacent_operators(self, expression):
        operators = ('*', '+', '-', '/')
        for char in expression
            if expression[i] in operators and expression[i-1] in operators:
                raise I_P_Error("No adjacent operators")
            if isinstance(expression[i], int) and isinstance(expression[i-1], int):
                raise I_P_Error("No adjacent operands")

        


