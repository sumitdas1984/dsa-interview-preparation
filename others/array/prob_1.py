# Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.

# Note: The rightmost element is always a leader.

# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]
# Explanation: 17 is greater than all the elements to its right i.e., [4, 3, 5, 2], therefore 17 is a leader. 5 is greater than all the elements to its right i.e., [2], therefore 5 is a leader. 2 has no element to its right, therefore 2 is a leader.


# # solution time-space complexity
# # time: O(n^2)
# # space: O(n)
# def find_leader(arr):
#     n = len(arr)
#     results = []
#     for i in range(n):
#         for j in range(i+1, n):
#             if arr[i] < arr[j]:
#                 break           
#         else:
#             results.append(arr[i])
#     return results


# solution time-space complexity
# time: O(n)
# space: O(n)
def find_leader(arr):
    result = []
    n = len(arr)
    max_right = arr[-1]
    result.append(max_right)
    for i in range(n-2, -1, -1):
        if arr[i] > max_right:
            max_right = arr[i]
            result.append(max_right)
    result.reverse()
    return result


input_arr = [16, 17, 4, 3, 5, 2]
result = find_leader(input_arr)
print(f"leaders: {result}")