#!/usr/bin/env python3
import regex

# This is an experiment using another regex library which supports recursive matches
# TODO: Figure out why the pattern is ignoring the outliers

def is_valid(str_input) :
    """Checks input string and returns whether parentheses sets are valid or not
    
    Args:
        str_input (string) Input String
    Returns:
        (bool) True - Valid, False - Invalid
    """

    # regex_paren_pattern = r"\(.*\)"
    # regex_brace_pattern = r"\{.*\}"
    # regex_bracket_pattern = r"\[.*\]"

    regex_pattern = r"\(([^()]*|(?R))*\)|\{([^{}]*|(?R))*\}|\[([^\[\]]*|(?R))*\]"
    
    match = regex.search(regex_pattern, str_input)

    print(match.groups())
    # if match:
    #     print(match.group())
    # else :
    #     print("No Match Found")

is_valid("()")
is_valid("())")
is_valid("()()")