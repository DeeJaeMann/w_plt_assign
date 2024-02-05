#!/usr/bin/env python3.12
import re

# How can you make this more scalable and reusable later?

def split_digits(int_num) :
    lst_result = []

    # Iterate through the number (as a string) and match each digit
    for str_digit in re.findall(r'\d', f"{int_num}") :
        lst_result.append(str_digit)

    return lst_result

def find_armstrong_numbers(numbers):
    lst_result = []

    for int_num in numbers :
        int_this_num = int_num

        lst_this_num_digits = split_digits(int_this_num)

        print(lst_this_num_digits)        
    
    return lst_result



print(find_armstrong_numbers([1,22,333]))