arr = [34, 12, 56, 286, 89, 23, 78, 57]

n = len(arr)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if not swapped:
        break
print("Sorted array is: ", arr)