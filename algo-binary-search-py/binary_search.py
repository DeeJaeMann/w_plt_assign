#!/usr/bin/env python3.12
def binary_search(value_to_find, array_to_search_through):
    # your code here
    
    # Linear search code
    # Iterate through the array and determine if the value to find is present
    # for int_index, str_element in enumerate(array_to_search_through) :

    #     if value_to_find == str_element :
    #         return int_index
        
    # return None
    # End Linear search code

    left = 0
    right = len(array_to_search_through) - 1

    while left <= right :
        mid = (left + right) // 2

        if array_to_search_through[mid] == value_to_find :
            return mid
        elif array_to_search_through[mid] < value_to_find :
            left = mid + 1
        else :
            right = mid - 1
    
    return None

def binary_search_global(value_to_find, array_to_search_through):
    # your code here
    # Linear global search code
    # lst_result = []

    # for int_index, str_element in enumerate(array_to_search_through) :

    #     if value_to_find == str_element :
    #         lst_result.append(int_index)

    # return lst_result
    # End linear global search code
    pass

print(binary_search("a", ["a", "b", "c"]))

print(binary_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]))