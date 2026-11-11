from stack import Stack
from infix_converter import InfixToPostfixConverter
from postfix_evaluator import PostfixEvaluator


def main():
    print("----- Postfix Evaluator -----")
    test_00 = PostfixEvaluator([5, 3, '+'])
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

    test_06 = PostfixEvaluator([26, 28,'+',32,2,';','-',5,'/'])
    test_06.eval_postfix()

    test_07 = PostfixEvaluator([2, 3,4,'+'])
    test_07.eval_postfix()

    test_08 = PostfixEvaluator([20, 29,9,'*',';'])
    test_08.eval_postfix()

    test_09 = PostfixEvaluator([25,23,'-','+'])
    test_09.eval_postfix()

    test_10 = PostfixEvaluator([8,0,'/'])
    test_10.eval_postfix()

    test_11 = PostfixEvaluator([5,'+'])
    test_11.eval_postfix()

    test_12 = PostfixEvaluator([3,'+',4])
    test_12.eval_postfix()

    print("\n----- Infix to Postfix Converter -----")

    test_13 = InfixToPostfixConverter(['A','+','B','*','C'])
    test_13.convert_to_postfix()

    test_14 = InfixToPostfixConverter(['(','A','+','B',')','*','C'])
    test_14.convert_to_postfix()

    test_15 = InfixToPostfixConverter(['A','*','B','+','C','/','D'])
    test_15.convert_to_postfix()

    test_16 = InfixToPostfixConverter(['(','A','+','B',')','*','(','C','-','D',')'])
    test_16.convert_to_postfix()

    test_17 = InfixToPostfixConverter(['A','+','B','*','C','-','D','/', 'E'])
    test_17.convert_to_postfix()

    test_18 = InfixToPostfixConverter(['A','*','(','B','+','C',')','/','D'])
    test_18.convert_to_postfix()

    test_19 = InfixToPostfixConverter(['(','A','+','B','*','C',')','/','(','D','-','E',')'])
    test_19.convert_to_postfix()

    test_20 = InfixToPostfixConverter(['A','+','(','B','-','C',')','*','D'])
    test_20.convert_to_postfix()

    test_21 = InfixToPostfixConverter(['(','A','+','B','*','(','C','-','D',')',')','/','E'])
    test_21.convert_to_postfix()

    test_22 = InfixToPostfixConverter(['A','+','B',')','C'])
    test_22.convert_to_postfix()

    test_23 = InfixToPostfixConverter(['A','+','B',';','C'])
    test_23.convert_to_postfix()
    
    test_24 = InfixToPostfixConverter(['+','A','B'])
    test_24.convert_to_postfix()

    test_25 = InfixToPostfixConverter(['A','+','*','B'])
    test_25.convert_to_postfix()

    test_26 = InfixToPostfixConverter(['A','B','+','C'])
    test_26.convert_to_postfix()

    test_27 = InfixToPostfixConverter(['A','+',')','B','*','C'])
    test_27.convert_to_postfix()
    
    test_28 = InfixToPostfixConverter(['(','A','+','B'])
    test_28.convert_to_postfix()

    test_29 = InfixToPostfixConverter(['A','+','B',')'])
    test_29.convert_to_postfix()

    #test_08 = PostfixEvaluator([0,8,'+'])
    #test_08.eval_postfix()
if __name__ == "__main__":
    main()
