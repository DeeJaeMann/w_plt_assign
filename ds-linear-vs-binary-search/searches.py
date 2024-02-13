#!/usr/bin/env python3.12

def linear_search_unsorted(lst_arr, str_target):
    int_steps = 0
    for str_element in lst_arr :
        int_steps += 1
        if str_element == str_target :
            return str_element

def binary_search_unsorted(lst_arr, str_target):
    int_steps = 0
    left = 0
    right = len(lst_arr)-1

    # This should be checking <= to ensure the last iteration checks
    # We check 'mid' so if we need to bracket to left and right being
    # equal, we have to factor that in
    while left <= right :
        int_steps += 1

        # Set the mid to half way between left and right
        mid = (left + right)//2
        # check the element at mid
        this_num = lst_arr[mid]
        if this_num == str_target :
            return f"Found {str_target} in {int_steps} steps"
        elif this_num < str_target :
            # Look right, change left limit
            # Change our left limits to the middle + 1
            left = mid + 1
        else :
            # Look left, change right limit
            # Change our right limits to the middle - 1
            right = mid - 1

        # print(f"Left: {left} Right: {right} Mid: {mid}")
    return -1

lst_unsorted = [42, 15, 7, 30, 22, 10, 18]
int_target = 30

# print(binary_search_unsorted(sorted(lst_unsorted), int_target))
# print(binary_search_unsorted(lst_unsorted, int_target))

def linear_search_sorted_words(word_list, target_word) :
    steps = 0
    for word in word_list :
        steps += 1
        if word == target_word :
            return 1
        return -1
    


