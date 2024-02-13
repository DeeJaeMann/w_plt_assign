#!/usr/bin/env python3.12
def linear_search(value_to_find, array_to_search_through):
    # your code here
    
    # Iterate through the array and determine if the value to find is present
    for int_index, str_element in enumerate(array_to_search_through) :

        if value_to_find == str_element :
            return int_index
        
    return None

def linear_search_global(value_to_find, array_to_search_through):
    # your code here
    lst_result = []

    for int_index, str_element in enumerate(array_to_search_through) :

        if value_to_find == str_element :
            lst_result.append(int_index)

    return lst_result

print(linear_search("a", ["a", "b", "c"]))

print(linear_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]))