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
    lst_opens = re.findall(r"\(|\[|\{", str_input)
    lst_closes = re.findall(r"\)|\]|\}", str_input)

    # check if the list is an even number
    if (len(lst_opens) + len(lst_closes)) % 2 != 0 :
        # it isn't, we don't have balanced sets
        return False
    elif len(lst_opens) != len(lst_closes) :
        return False

    return True

    # print(lst_matches)



print(is_valid("()"))
print(is_valid("())"))
print(is_valid("()()"))
print(is_valid("(["))