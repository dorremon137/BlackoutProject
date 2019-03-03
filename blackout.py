"""
Author: Phuvit Kittisapkajon
"""
from rit_lib import*
from myStack import*

def priority(x):
    """
    This function give the operator a priority where *'s and /'s priority is higher than +'s and -'s one.

    :param x: operator
    :return: operator's priority
    """
    if x is "*" or x is "/":
        return 2
    elif x is "+" or x is "-":
        return 1
    else:
        return 0

def empty_checker(Stack):
    """
    This function checks if the stack is empty

    :param Stack: stack
    :return: Boolean True or False
    """
    if Stack is None:
        return True
    else:
        return False


def compute(s):
    """
    This function computes the value of string 's', which represents either the left or right
    side of an equation. Function "empty_checker(Stack)" is present in this function to check whether
    the operator stack or the operant stack is empty.

    :param s: a string
    :return: a numeric value or None if the equation if not valid.
    """
    operantStack = None
    operatorStack = None
    number = ""
    for x in s:
        if x.isdigit():
            number += x
        elif x is "*" or x is "/" or x is "+" or x is "-":
            if number != "":
                operantStack = push(operantStack, number)
                number = ""
            if empty_checker(operatorStack) is False:
                while priority(top(operatorStack)) >= priority(x):
                    if empty_checker(operantStack) is False:
                        value2 = top(operantStack)
                        if type(value2) is str:
                            value2 = int(value2)
                        operantStack = pop(operantStack)
                    else:
                        return None
                    if empty_checker(operantStack) is False:
                        value1 = top(operantStack)
                        if type(value1) is str:
                            value1 = int(value1)
                        operantStack = pop(operantStack)
                    else:
                        return None
                    operator = top(operatorStack)
                    if operator == "*":
                        result = value1 * value2
                    elif operator =="/":
                        result = value1 / value2
                    elif operator == "+":
                        result = value1 + value2
                    elif operator == "-":
                        result = value1 - value2
                    operantStack = push(operantStack,result)
                    operatorStack = pop(operatorStack)
                    result = 0
                    if empty_checker(operatorStack) is True:
                        break
            operatorStack = push(operatorStack,x)
        elif x == "(":
            operatorStack = push(operatorStack,x)
        elif x == ")":
            if number != '':
                operantStack = push(operantStack, number)
                number = ""
            if empty_checker(operatorStack) is False:
                while top(operatorStack) != "(":
                    if empty_checker(operantStack) is False:
                        value2 = top(operantStack)
                        if type(value2) is str:
                            value2 = int(value2)
                        operantStack = pop(operantStack)
                    else:
                        return None
                    if empty_checker(operantStack) is False:
                        value1 = top(operantStack)
                        if type(value1) is str:
                            value1 = int(value1)
                        operantStack = pop(operantStack)
                    else:
                        return None
                    operator = top(operatorStack)
                    if operator == "*":
                        result = value1 * value2
                    elif operator == "/":
                        result = value1 / value2
                    elif operator == "+":
                        result = value1 + value2
                    elif operator == "-":
                        result = value1 - value2
                    operantStack = push(operantStack, result)
                    result = 0
                    operatorStack = pop(operatorStack)
                    if empty_checker(operatorStack) is True:
                        return None
            if empty_checker(operatorStack) is True:
                return None
            else:
                operatorStack = pop(operatorStack)
                if empty_checker(operatorStack) is True:
                    return None
                elif top(operatorStack) == None and top(operantStack) == None:
                    return None
    if number != "":
        operantStack = push(operantStack, number)
    while operatorStack != None:
        if empty_checker(operantStack) is False:
            value2 = top(operantStack)
            if type(value2) is str:
                value2 = int(value2)
            operantStack = pop(operantStack)
        else:
            return None
        if empty_checker(operantStack) is False:
            value1 = top(operantStack)
            if type(value1) is str:
                value1 = int(value1)
            operantStack = pop(operantStack)
        else:
            return None
        operator = top(operatorStack)
        if operator == "*":
            result = value1 * value2
        elif operator == "/":
            result = value1 / value2
        elif operator == "+":
            result = value1 + value2
        elif operator == "-":
            result = value1 - value2
        elif operator == "(":
            return None
        operantStack = push(operantStack, result)
        result = 0
        operatorStack = pop(operatorStack)
    if empty_checker(operantStack) is False:
        if type(top(operantStack)) is str:
            return int(top(operantStack))
        else:
            return top(operantStack)
    else:
        return None

def evaluate(s):
    """
    This function will evaluate a string representing an entire equation to determine if it is valid.
    If the equation is syntactically valid. and the left and right sides are equal, then this function
    will return True. Otherwise, it returns False.

    :param s: a string representing an entire equation
    :return: Boolean True ff the equation is syntactically valid. Else, Return False
    """
    if s == "":
        return False
    if s[0] == "=":
        return False
    if len(s) < 3:
        return False
    s_copy = s[:]
    while s_copy != "":
        if s_copy[0] == "=":
            break
        else:
            s_copy = s_copy[1:]
    if s_copy == "":
        return False
    left, right = s.split("=")
    left_result = compute(left)
    if left_result is None or left_result is '':
        return False
    right_result = compute(right)
    if right_result is None or left_result is '':
        return False
    if float(left_result) == float(right_result):
        return True
    else:
        return False

def solve(s):
    """
    This function will solve a given puzzle, represented by the string s. It will black out two squares
    at a time, passing each possible combination to the test function. It should return the first valid
    solution it finds, or None if not valid solution exists.

    :param s: a given puzzle
    :return: the first valid solution it finds, or None if not valid solution exists.
    """
    for i in range(len(s)):
        if s[i] == "=":
            pass
        else:
            si1 = s[0:i]
            si2 = s[i + 1:]
            si3 = si1 + si2
            for j in range (len(si3)):
                if si3[j] == "=":
                    pass
                else:
                    sj1 = si3[0:j]
                    sj2 = si3[j + 1:]
                    sj3 = sj1 + sj2
                    if evaluate(sj3) is True:
                        return sj3
                    else:
                        pass
    return None

def main():
    """
    This function is the main function for the first part of blackout. Its prompt for and read the file one
    line at a time and submit each line, or puzzles. to be solved at a time. It prints out the puzzles and
    the solution when it found.
    """
    file = input("Enter the text file (EX. puzzles.txt):")
    for lines in open(file):
        line = lines.strip()
        print("")
        print("Given Equation:",line)
        print("Solution:",solve(line))

def compute_test():
    """
    This function tests the compute function.
    """
    string1 = "28/2"
    string2 = "63-2-9"
    string3 = "6*(15-3)"
    string4 = "282"
    string5 = "269+16*16"
    string6 = "18*2*2+2"
    string7 = "100-7*2*2*2"
    string8 = "26+16*16"
    print("Begin compute_test")
    print(compute(string1) == 14)
    print(compute(string2) == 52)
    print(compute(string3) == 72)
    print(compute(string4) == 282)
    print(compute(string5) == 525)
    print(compute(string6) == 74)
    print(compute(string7) == 44)
    print(compute(string8) == 282)
    print(compute("(2)") == 2)
    print(compute("2()") == None)
    print(compute("()2") == None)
    print(compute("9)-6(") == None)

def evaluate_test():
    """
    This function tests the evaluate function.
    """
    string1 = "28/2=269+16*16"
    string2 = "63-2-9=18*2*2+2"
    string3 = "6*(15-3)=100-7*2*2*2"
    string4 = "282=26+16*16"

    print("Begin evaluate_test")
    print(evaluate(string1) == False)
    print(evaluate(string2) == False)
    print(evaluate(string3) == False)
    print(evaluate(string4) == True)
    print("End evaluate_test")

def solve_test():
    """
    This function tests the evaluate function.
    """
    string1 = "28/2=269+16*16"
    string2 = "63-2-9=18*2*2+2"
    string3 = "6*(15-3)=100-7*2*2*2"

    print("Begin solve_test")
    print(solve(string1) == "282=26+16*16")
    print(solve(string2) == "63-29=8*2*2+2")
    print(solve(string3) == "6*(15-3)=100-7*2*2")
    print("End solve_tree")
if __name__ == '__main__':
    main()



