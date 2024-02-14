def linear_search(value_to_find, array_to_search_through):
    for index in range(len(array_to_search_through)):
        if array_to_search_through[index] == value_to_find:
            return index

def linear_search_global(value_to_find, array_to_search_through, pivot, direction="fwd"):
    # Expected values for multiplier 1 (add) or -1 (subtract)
    # print(value_to_find)
    result = []
    steps = 0
    for index in range(len(array_to_search_through)):
        steps += 1
        # print(array_to_search_through[index])
        if array_to_search_through[index] == value_to_find:
            if direction == "back":
                print(f"Back index: {index}")
                result.append(pivot - (index + 1))
            else:
                print(f"Fwd Index: {index}")
                result.append(pivot + (index+1))
        else:
            return [sorted(result), steps]
    return [sorted(result), steps]


def binary_search_global(target, arr):
    left = 0
    right = len(arr) - 1
    steps = 0
    while left <= right:
        steps += 1
        middle = (left + right)//2
        if arr[middle] == target:
            return check_up_and_back(middle, arr, steps)   # <--- Identified split
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1


def check_up_and_back(pivot: int, arr: list, steps):
    # print(pivot)
    back_arr = arr[pivot-1::-1]
    print(f"Back array {back_arr}")
    forward_arr = arr[pivot+1:]

    # print(forward)
    back_list = linear_search_global(arr[pivot],back_arr, pivot, "back")

    front_list = linear_search_global(arr[pivot], forward_arr, pivot)

    steps += back_list[1]
    steps += front_list[1]
    # # return [linear_search_global(arr[pivot],back_arr, pivot, "back")[0] + [pivot] + linear_search_global(arr[pivot], forward_arr, pivot)[0], steps + ]
    final = back_list[0] + [pivot] + front_list[0]
    return [final, steps]

print(sorted(["b", "a", "n", "a", "n", "a", "s", "a", "a", "b", "z"]))
print(binary_search_global('n', sorted(["b", "a", "n", "a", "n", "a", "s", "a", "a", "b", "z"])))
