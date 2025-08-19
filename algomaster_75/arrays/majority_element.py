# # Hashmap based solution || time complexity: O(n), space complexity: O(n)
# def find_majority_element(nums):
#     counts = {}
#     for num in nums:
#         if num not in counts:
#             counts[num] = 1
#         else:
#             counts[num] += 1
#         if counts[num] > len(nums)//2:
#             return num


# # Soring based solution || time complexity: O(nlogn), space complexity: O(1) or O(n)
# def find_majority_element(nums):
#     nums.sort()
#     return nums[len(nums)//2]


# Boyer-Moore Voting algo || time complexity: O(n), space complexity: O(1)
def find_majority_element(nums):
    count = 0
    candidate = None

    for idx,num in enumerate(nums):
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
        # pass

    return candidate

nums = [2,2,1,1,1,2,2]
majority_element = find_majority_element(nums)
print(f"majority element: {majority_element}")