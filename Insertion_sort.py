"""
To implement the Insertion Sort algorithm in a programming language, we need:

1. An array with values to sort.
2. An outer loop that picks a value to be sorted. For an array with n values, this outer loop skips the first value, and must run n-1 times.
An inner loop that goes through the sorted part of the array, to find where to insert the value. If the value to be sorted is at index i, 
the sorted part of the array starts at index 0 and ends at index i-1.
"""

arr = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(arr)
for i in range(1,n):
    insert_index = i
    current_value = arr.pop(i)
    for j in range(i-1, -1, -1):
        if arr[j] > current_value:
            insert_index = j
    arr.insert(insert_index, current_value)
    
print("Sorted array:", arr)