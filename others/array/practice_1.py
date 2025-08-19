# reverse array using auxiliary space
# reverse array using swap

def reverse_array_auxiliary(arr):
    n = len(arr)
    aux = [0]*n
    for i in range(n):
        aux[i] = arr[n-1-i]
    
    for i in range(n):
        arr[i] = aux[i]

    return arr


def reverse_array_swap(arr):
    left = 0
    right = len(arr)-1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr


arr = [1,2,3,4,5]
print("original array: ", arr)

# reversed_arr_aux = reverse_array_auxiliary(arr)
# print("reversed array using auxiliary: ", reversed_arr_aux)

reversed_arr_swap = reverse_array_swap(arr)
print("reversed array using swap: ", reversed_arr_swap)
