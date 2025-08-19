# Hashmap based brute force solution || time complexity: O(n), space complexity: O(n)
def find_majority_element_hashmap(nums):
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
        if counts[num] > len(nums)//2:
            return num


# Sorting based solution || time complexity: O(nlogn), space complexity: O(1) or O(n)
def find_majority_element_sorting(nums):
    nums.sort()
    return nums[len(nums)//2]


# Boyer-Moore Voting algo || time complexity: O(n), space complexity: O(1)
def find_majority_element_voting(nums):
    count = 0
    candidate = None

    for idx,num in enumerate(nums):
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

nums = [2,2,1,1,1,2,2]

majority_element = find_majority_element_hashmap(nums)
print(f"majority element (hashmap): {majority_element}")

majority_element = find_majority_element_sorting(nums)
print(f"majority element (sorting): {majority_element}")

majority_element = find_majority_element_voting(nums)
print(f"majority element (voting): {majority_element}")