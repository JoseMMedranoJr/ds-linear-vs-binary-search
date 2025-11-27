

# def linear_search_last_occurrence(arr, target):
#     steps = 0
#     for i, element in enumerate(arr):
#         steps += 1
#         if element == target:
#             return i, steps  # Return the index and steps taken if found
#     return -1, steps  

Binary Search
def binary_search_last_occurrence(arr, target):
    low = 0
    high = len(arr) -1
    setps = 0
    last_occur = -1
  
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if target == arr[mid]:
              last_occur = mid
              low = mid + 1
        elif arr[mid] < target:
                 low = mid + 1
        else:
             high = mid -1
        
    return last_occur, steps 

# Scenario 3 Test
occurrence_list = [5, 10, 15, 20, 10, 25, 30, 35, 10, 40]
target_3 = 10
# result_linear_search_3 = linear_search_last_occurrence(occurrence_list, target_3)
# result_binary_search_3 = binary_search_last_occurrence(sorted(occurrence_list), target_3)
# print(f"Scenario 3 (Linear Search): Last occurrence of {target_3} found at index {result_linear_search_3[0]} in {result_linear_search_3[1]} steps.")
print(f"Scenario 3 (Binary Search): Last occurrence of {target_3} found at index {result_binary_search_3[0]} in {result_binary_search_3[1]} steps.")
