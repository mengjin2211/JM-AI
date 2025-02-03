import random

def quickselect(arr, k):
    if len(arr) == 1:
        return arr[0]

    # Choose a random pivot to avoid worst-case scenarios on already sorted arrays
    pivot = random.choice(arr)

    # Partition the array
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Find which part of the array contains the k-th element
    if k <= len(left):
        return quickselect(left, k)
    elif k > len(left) + len(middle):
        return quickselect(right, k - len(left) - len(middle))
    else:
        # If k is in the middle group, return the pivot
        return pivot




def in_place_quickselect(arr, k):
    if not arr:
        return None
    k = k - 1
    def partition(low, high):
        pivot = arr[high]
        i = low
        for j in range(low, high):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[high] = arr[high], arr[i]
        return i

    low, high = 0, len(arr) - 1
    while low <= high:
        pivot_index = partition(low, high)
        if pivot_index == k:
            return arr[pivot_index]
        elif pivot_index < k:
            low = pivot_index + 1
        else:
            high = pivot_index - 1

