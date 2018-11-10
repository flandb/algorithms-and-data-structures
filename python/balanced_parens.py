"""
From 'The Algorithm Design Manual' by Steven S. Skiena

3-1. [3] A common problem for compilers and text editors is determining
whether the parentheses in a string are balanced and properly nested. For
example, the string ((())())() contains properly nested pairs of parentheses,
which the strings )()( and ()) do not. Give an algorithm that returns true
if a string contains properly nested and balanced parentheses, and false if
otherwise. For full credit, identify the position of the first offending
parenthesis if the string is not properly nested and balanced.

INPUT:  string -- empty or one containing only '(' and ')' chars.
OUTPUT: boolean -- True if every open paren '(' has matching close paren ')',
        False (and print index of first offending paren) if not.
NOTES:  if odd number of parens (unbalanced), can't shortcut False return val
        with modulus 2 check because index of first offending paren needed.

TODO: Runtime analyses.
"""

from stack import Stack


# Recursive solution
def balanced_parens_rec(parens_str=''):
    """
    Return True if parens are balanced; False otherwise.

    If False, output index of first offending parenthesis without match.
    TODO: Debug.
    TODO: Add unit tests.
    """

    # Empty strings are considered balanced
    if not parens_str:
        return True

    # False if first char is closing paren, or only one paren in string
    if parens_str[0] == ')' or len(parens_str) == 1:
        print('Index of first unmatched parenthesis: 0')
        return False

    def rec_helper(parens_str, open_parens_pos, i):
        """
        Track position of most recent unmatched paren to return if unbalanced.
        """

        # Base case
        if not parens_str:
            if not open_parens_pos:
                return True
            else:
                print(
                    'Index of first unmatched parenthesis: ' +
                    str(open_parens_pos.pop())
                )
                return False

        if parens_str[0] == ')':
            if open_parens_pos:
                # Match -- remove index of most recent unmatched open paren.
                open_parens_pos.pop()
                return rec_helper(
                    parens_str[1:],
                    open_parens_pos,
                    i + 1
                )
            else:
                # No current unmatched open paren to match close paren.
                print(f'Index of first unmatched parenthesis: {i}')
                return False
        else:
            # Add index of open paren to top of stack; most recent unmatched.
            open_parens_pos.push(i)
            return rec_helper(
                parens_str[1:],
                open_parens_pos,
                i + 1
            )

    return rec_helper(parens_str, Stack(), 0)


# Iterative solution using Stack
def balanced_parens_iter(parens_str=''):
    """
    Return True if parens are balanced; False otherwise.

    If False, output index of first offending parenthesis without match.
    TODO: Add unit tests
    """

    # Empty strings are considered True
    if not parens_str:
        return True

    # Holds opening parentheses '(' -- removed if match found
    stack = Stack()

    # 'stack' variable keeps track of indices that contain opening parens
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
