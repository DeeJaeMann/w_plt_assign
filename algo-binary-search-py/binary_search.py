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

    # ["b", "a", "n", "a", "n", "a", "s"]
    #   L              M              R
    # Issues:  if it finds on the 1st, it doesn't know if it has all matches
    #  needs to run on sorted list
    # ["a", "a", "a", "b", "n", "n", "s"] (sorted)
    #   L              M              R
    #  Will check Left
    # ["a", "a", "a", "b", "n", "n", "s"] (sorted)
    #   L    M         R
    #  Will find a match here, do we continue to pass through?  Which way do we go?
    # ["a", "a", "a", "b", "n", "n", "s"] (sorted) 
    #  L/M   R    *
    #  If we go left, we'll miss the occurance on the right (index 2)
    #
    #  Do we enter linear to check each element at this point?
    #   What is the most effective method to reset left and right limits?
    #
    #  What alternatives are there to try to maintain speed?
    pass

print(binary_search("a", ["a", "b", "c"]))

print(binary_search_global("a", ["b", "a", "n", "a", "n", "a", "s"]))