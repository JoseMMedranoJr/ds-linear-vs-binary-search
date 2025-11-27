# # Linear Search
# def linear_search_last_occurrence(arr, target):
#     # Your code here
#     pass

def linear_search_last_ch(arr, target):
    steps = 0
    for i, element in enumerate(arr):
        steps += 1
        if element == target:
            return i, steps  # Return the index and steps taken if found
    return -1, steps  

# # Binary Search
# def binary_search_last_occurrence(arr, target):
#     # Your code here
#     pass

# Binary Search
# def binary_search_occurence(arr, target):
#     sorted_list = sort(unsorted_list)
#     count = 0
#     low = 0
#     high = len(sorted_list) - 1

#     while low <= high:
#         mid = (low + high) // 2

#     if sorted_list[mid] == target:


# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
# result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")
