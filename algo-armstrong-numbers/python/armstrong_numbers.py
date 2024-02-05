#!/usr/bin/env python3.12
import re

# How can you make this more scalable and reusable later?

#Begin Helper Functions

'''
    This function splits the digits of a number into an array
    @param {int} int_num Number to be split
    @returns Array of digits from int_num
'''
def split_digits(int_num) :
    lst_result = []

    # Iterate through the number (as a string) and match each digit
    for str_digit in re.findall(r'\d', f"{int_num}") :
        lst_result.append(str_digit)

    return lst_result

''' 
    This function calculates the total of each digit of a list calculated to the
    power of the list length
    @param {list} lst_digits List of digits to calculate
    @returns Calculated total of digits to the power of the length of the list
'''
def calculate_number(lst_digits) :
    int_total = 0
    lst_subtotals = []

    # Iterate through lst_digits and calculate the digits to the power of the length of the list
    for int_digit in lst_digits :
        int_this_subtotal = pow(int(int_digit), len(lst_digits))

        lst_subtotals.append(int_this_subtotal)

    for int_digit in lst_subtotals :
        int_total += int_digit

    return int_total

# End Helper Functions

'''
    This function accepts a range of numbrers as a list and returns the Armstrong Numbers
    found in that list
    @param {list} numbers List of a range of numbers to search
    @returns List containing Armstrong Numbers found in the given list
'''
def find_armstrong_numbers(numbers):
    lst_result = []

    for int_num in numbers :
        int_this_num = int_num

        lst_this_num_digits = split_digits(int_this_num)

        int_this_total = calculate_number(lst_this_num_digits)  

        if int_this_total == int_this_num :
            lst_result.append(int_this_num)
    
    return lst_result



#print(find_armstrong_numbers([5,371,333]))