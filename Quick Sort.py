def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index-1)
        quicksort(arr, pivot_index+1, high)

my_arr = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_arr)
print("Sorted array:", my_arr)