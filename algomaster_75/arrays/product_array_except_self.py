import math

# Bruteforce solution | time: O(n^2), space: O(n) 
def product_except_self_bruteforce(arr):
    n = len(arr)
    result = [1]*n
    for i in range(n):
        for j in range(n):
            if i!=j:
                result[i] *= arr[j]
    return result


# Improved solution | time: O(n), space: O(n) 
def product_except_self_prefix_suffix(arr):
    length = len(arr)
    output = [1]*length
    prefix_product = [1]*length
    suffix_product = [1]*length

    for i in range(1, length):
        prefix_product[i] = prefix_product[i-1] * arr[i-1]
    for i in range(length-2, -1, -1):
        suffix_product[i] = suffix_product[i+1] * arr[i+1]
    
    for i in range(length):
        output[i] = prefix_product[i] * suffix_product[i]

    return output


nums = [1,2,3,4,5]
answer = product_except_self_bruteforce(nums)
print("answer bruteforce: ", answer)
answer = product_except_self_prefix_suffix(nums)
print("answer prefix_suffix: ", answer)