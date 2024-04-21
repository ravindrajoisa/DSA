"""To implement the Radix Sort algorithm we need:

An array with non negative integers that needs to be sorted.
A two dimensional array with index 0 to 9 to hold values with the current radix in focus.
A loop that takes values from the unsorted array and places them in the correct position in the two dimensional radix array.
A loop that puts values back into the initial array from the radix array.
An outer loop that runs as many times as there are digits in the highest value."""

myArray = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", myArray)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxValue = max(myArray)
exp = 1

while maxValue // exp > 0:

    while len(myArray) > 0:
        val = myArray.pop()
        radixIndex = (val // exp) % 10
        radixArray[radixIndex].append(val)

    for bucket in radixArray:
        while len(bucket) > 0:
            val = bucket.pop()
            myArray.append(val)

    exp *= 10

print("Sorted array:", myArray)

#code works online.