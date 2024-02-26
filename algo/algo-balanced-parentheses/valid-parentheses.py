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

    lst_opens = sorted(lst_opens)
    lst_closes = sorted(lst_closes)

    # check if the list is an even number
    if (len(lst_opens) + len(lst_closes)) % 2 != 0 :
        # it isn't, we don't have balanced sets
        return False
    elif len(lst_opens) != len(lst_closes) :
        return False
    else :
        # compare the matches
        for int_index, char in enumerate(lst_opens) :
            match char:
                case '(':
                    if lst_closes[int_index] != ')' :
                        return False

                case '[':
                    if lst_closes[int_index] != ']' :
                        return False

                case '{':
                    if lst_closes[int_index] != '}' :
                        return False

    return True


print(is_valid("()"))
print(is_valid("())"))
print(is_valid("()()"))
print(is_valid("({()()[]})"))