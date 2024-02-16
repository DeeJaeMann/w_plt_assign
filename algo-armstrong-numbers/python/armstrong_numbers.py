#!/usr/bin/env python3.12
import re

# How can you make this more scalable and reusable later?

#Begin Helper Functions

def split_digits(int_num) :
    """This function splits the digits of a number into a list

    Args:
        int_num (int) Number to be split
    Returns:
        (list) List of digits from int_num
    """
    lst_result = []

    # Iterate through the number (as a string) and match each digit
    for str_digit in re.findall(r'\d', f"{int_num}") :
        lst_result.append(str_digit)

    return lst_result

def calculate_number(lst_digits) :
    """This function calculates the total of each digit of a list calculated to the power of the list length

    Args:
        lst_digits (list) List of digits to calculate
    Returns:
        (int) Calculated total of digits to the power of the length of the list
    """
    int_total = 0
    lst_subtotals = []

    # Iterate through lst_digits and calculate the digits to the power of the length of the list
    for int_digit in lst_digits :
        int_this_subtotal = pow(int(int_digit), len(lst_digits))

        # Add this subtotal to the list of subtotals
        lst_subtotals.append(int_this_subtotal)

    # Calculate the sum of all of the subtotals
    # TODO: Can this use Reduce?
    for int_digit in lst_subtotals :
        int_total += int_digit

    return int_total

# End Helper Functions

def find_armstrong_numbers(numbers):
    """This function accepts a range of numbers as a list and returns the Armstrong Numbers found in that list

    Args:
        numbers - (list) A range of numbers to search
    Returns:
        (list) List containing Armstrong Numbers found in numbers
    """
    lst_result = []

    for int_num in numbers :
        # TODO: Why did I make this variable?
        int_this_num = int_num

        # split each of the digits of this number into a list
        lst_this_num_digits = split_digits(int_this_num)

        # Calculate the total of this digit to the power of the list length
        int_this_total = calculate_number(lst_this_num_digits)  

        # Compare the previous total to the current number
        if int_this_total == int_this_num :
            lst_result.append(int_this_num)
    
    return lst_result



#print(find_armstrong_numbers([5,371,333]))