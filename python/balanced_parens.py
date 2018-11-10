"""
From 'The Algorithm Design Manual' by Steven S. Skiena

3-1. [3] A common problem for compilers and text editors is determining
whether the parentheses in a string are balanced and properly nested. For
example, the string ((())())() contains properly nested pairs of parentheses,
which the strings )()( and ()) do not. Give an algorithm that returns true
if a string contains properly nested and balanced parentheses, and false if
otherwise. For full credit, identify the position of the first offending
parenthesis if the string is not properly nested and balanced.
"""

from stack import Stack


# Recursive solution
def balanced_parens_rec(parens_str=''):
    """
    Returns True if parens are balanced;
    False otherwise, with printed index of offending paranthesis.
    TODO: Debug
    TODO: Add unit tests
    """

    # Empty strings are considered balanced
    if not parens_str:
        return True

    if parens_str[0] == ')' or len(parens_str) == 1:
        print('Index of first unmatched parenthesis: 0')
        return False

    def rec_helper(parens_str, i):
        """
        Keep track of opening paren positions in var i so first instance
        of unmatched paren can be output if string unbalanced.
        """

        # Base case
        if not parens_str:
            return True
        elif parens_str[0] == ')':
            return ')'
        elif len(parens_str) == 1:
            # Last character in string is closed paren, no match.
            print(f'Index of first unmatched parenthesis: {i}')
            return False

        if parens_str[0] + rec_helper(parens_str[1:], i + 1) == '()':
            if parens_str[2]:
                return rec_helper(parens_str[2:], i + 2)
            return True

        print(f'Index of first unmatched parenthesis: {i}')
        return False

    return rec_helper(parens_str, 0)


# Iterative solution using Stack
def balanced_parens_iter(parens_str=''):
    """
    Returns True if parens are balanced;
    False otherwise, with printed index of offending paranthesis.
    TODO: Add unit tests
    """

    # Empty strings are considered True
    if not parens_str:
        return True

    # Holds opening parentheses '(' -- removed if match found
    stack = Stack()

    # 'stack' variable keeps track of indeces that contain opening parens
    # and omits the actual character (not needed)
    for i, paren in enumerate(parens_str):
        if paren == '(':
            stack.push(i)
        elif stack:
            stack.pop()
        else:
            print(f'Index of first unmatched parenthesis: {i}')
            return False

    # If stack not empty at end of string, unmatched paren(s) remain
    if stack:
        print(f'Index of first unmatched parenthesis: {stack.pop()}')
        return False

    return True
