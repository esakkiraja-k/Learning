#%% Imports and functions declaration
def sum_list(input_list: list) -> int:
    """
    Sums the values of a list
    :param input_list:
    :return: the sum of the values
    """
    result = 0
    for i in input_list:
        result += i
    return result


def sublist_generator(input_list: list) -> list:
    """
    Given a list generates all possible combinations
    :param input_list: input list
    :return: all possible combinations of lists
    """
    list_of_lists = []
    list_max_pos = len(input_list)+1

    for initial_sublist_pos in range(list_max_pos):
        for final_sublist_pos in range(initial_sublist_pos+1, list_max_pos):
            list_of_lists.append(input_list[initial_sublist_pos:final_sublist_pos])
    return list_of_lists


def max_sum_subarray(input_list: list)-> int:
    """
    Given a list, returns the maximum value issue from all possible combinations
    :param input_list: input list
    :return: maximum value issue form all elements combinations
    """
    max_val = -float("inf")
    list_of_lists = sublist_generator(input_list)

    for list in list_of_lists:
        list_added = sum_list(list)
        if list_added > max_val:
            max_val = list_added
    return max_val

def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    
    output = max_sum_subarray(arr)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arr= [1, 2, 3, -4, 6]
solution= 8 # sum of array

test_case = [arr, solution]
test_function(test_case)