#!/usr/bin/env python3
import re


def is_valid(str_input) :
    """Checks input string and returns whether parentheses sets are valid or not
    
    Args:
        str_input (string) Input String
    Returns:
        (bool) True - Valid, False - Invalid
    """
   
    # Match all parentheses, brackets and braces using non-capture groups
    # findall returns a list of all matches found
    lst_matches = re.findall(r"(?:\(|\))|(?:\[|\])|(?:\{|\})", str_input)

    # check if the list is an even number
    if len(lst_matches) % 2 != 0 :
        # it isn't, we don't have balanced sets
        return False

    return True

    # print(lst_matches)



print(is_valid("()"))
print(is_valid("())"))
print(is_valid("()()"))