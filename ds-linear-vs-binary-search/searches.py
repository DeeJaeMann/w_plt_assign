#!/usr/bin/env python3.12

def linear_search_unsorted(lst_arr, str_target):
    int_steps = 0
    lst_result = []
    for int_index in range(0, (len(lst_arr))) :
        int_steps += 1
        if lst_arr[int_index] == str_target :
            lst_result = [int_index, int_steps]
            return lst_result

def binary_search_unsorted(lst_arr, str_target):
    int_steps = 0
    left = 0
    right = len(lst_arr)-1
    lst_result = []

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
            lst_result = [mid, int_steps]
            return lst_result
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

result_linear_search_1 = linear_search_unsorted(lst_unsorted, int_target)
result_linear_search_2 = binary_search_unsorted(lst_unsorted, int_target)

print(f"Scenario 1 (Linear Search): Target {int_target} found at index {result_linear_search_1[0]} in {result_linear_search_1[1]} steps.")
print(f"Scenario 2 (Linear Search): Target {int_target} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")


def linear_search_sorted_words(word_list, target_word) :
    steps = 0
    lst_result = []
    for int_index in range(0, (len(word_list))) :
        word = word_list[int_index]
        steps += 1
        if word == target_word :
            lst_result.append(int_index)
            break
        
    lst_result.append(steps)
    return lst_result
    
def binary_search_sorted_words(word_list, target_word) :
    steps = 0
    lst_result = []

    left = 0
    right = len(word_list)

    while left <= right :
        steps += 1
        # Add left and right and divide the result by 2 (round down)
        # to get the middle point between the two
        mid = (left + right)//2

        if word_list[mid] == target_word :
            lst_result = [mid, steps]
            return lst_result
        elif word_list[mid] < target_word :
            left = mid + 1
        else :
            right = mid - 1

    return -1


sorted_word_list = ['apple', 'banana', 'cherry', 'grape', 'orange','strawberry']
target_2 = 'orange'

result_linear_search_2 = linear_search_sorted_words(sorted_word_list, target_2)
result_binary_search_2 = binary_search_sorted_words(sorted_word_list, target_2)

print(f"Scenario 2 (linear search): Target {target_2} found at index {result_linear_search_2[0]} in {result_linear_search_2[1]} steps.")
print(f"Scenario 2 (Binary Search): Target {target_2} found at index {result_binary_search_2[0]} in {result_binary_search_2[1]} steps.")

def linear_search_last_occurrence(arr, target) :
    steps = 0
    lst_indexes = []

    for int_index in range(len(arr)) :
        steps += 1
        if arr[int_index] ==  target :
            lst_indexes.append(int_index)
        
    if len(lst_indexes) > 0 :
        return [lst_indexes[-1], steps]

def binary_search_last_occurrence(arr, target) :

    steps = 0
    lst_indexes = []

    left = 0
    right = len(arr)

    while left <= right :
        steps += 1
        mid = (left + right)//2

        if arr[mid] == target :
            print(mid)

            left = mid
            

            break
        elif arr[mid] < target :
            left = mid + 1
        else :
            right = mid - 1

    return [arr[0], steps]

occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")