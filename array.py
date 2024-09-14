def max_subarray_sum(arr):
    max_current = max_global = arr[0]
    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        if max_current > max_global:
            max_global = max_current
    return max_global

arr = [-2, -3, 4, -1, -2, 1, 5, -3]
print(max_subarray_sum(arr))  # Output: 7