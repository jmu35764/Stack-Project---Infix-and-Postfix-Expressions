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

    #test_08 = PostfixEvaluator([0,8,'+'])
    #test_08.eval_postfix()
if __name__ == "__main__":
    main()
