#!/usr/bin/env python3.12
import re

def to_roman(num):
    # write your code here!
    str_output = ''
    int_divisor = 0

    dct_roman_to_arabic = {
        'M' : 1000,
        'D' : 500,
        'C' : 100,
        'L' : 50,
        'X' : 10,
        'V' : 5,
        'I' : 1,
    }

    lst_roman_priority = ['M','D','C','L','X','V','I']



    for str_element in lst_roman_priority :
        int_divisor = dct_roman_to_arabic[str_element]

        int_tmp_divide = num // int_divisor

        if(int_tmp_divide > 0) :
            str_output += str_element * int_tmp_divide

        num -= (int_divisor * int_tmp_divide)


    for int_index, str_element in enumerate(lst_roman_priority) :
        # Match any set of roman numerals that have 4 of the same numeral

        re_duplicates_pattern = re.compile(r'' + str_element + '{4}')
        if re_duplicates_pattern.search(str_output) :

            re_behind_pattern = re.compile(r'' + lst_roman_priority[int_index - 1] + lst_roman_priority[int_index] + '{4}')

            if re_behind_pattern.search(str_output) :

                str_output = re.sub(re_behind_pattern, lst_roman_priority[int_index] + lst_roman_priority[int_index - 2], str_output)
            else :

                str_output = re.sub(re_duplicates_pattern, lst_roman_priority[int_index] + lst_roman_priority[int_index-1], str_output)


    return str_output

#print(to_roman(944))