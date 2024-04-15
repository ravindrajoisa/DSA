def linearSearch(arr, targetValue):
    for i in range(len(arr)):
        if arr[i] == targetValue:
            return i
    return -1

arr = [3, 6, 8, 7]
targetValue = 7

result = linearSearch(arr, targetValue)

if result != -1:
    print("Value", targetValue, "found at index", result)
else:
    print("Value", targetValue, "not found")