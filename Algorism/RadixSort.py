
def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr[], so that arr now contains sorted numbers
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Find the maximum number to know the number of digits
    max1 = max(arr)

    # Do counting sort for every digit. Note that exp is 10^i where i is the current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Example usage
arr = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", arr)
radix_sort(arr)
print("Sorted array:", arr)


import matplotlib.pyplot as plt
import numpy as np

# Range of n values
n_values = np.linspace(1, 1000, 1000)

# O(n) function
linear_complexity = n_values

# O(n log n) function
n_log_n_complexity = n_values * np.log(n_values)

# Plotting the functions
plt.figure(figsize=(10, 6))
plt.plot(n_values, linear_complexity, label='O(n)', color='blue')
plt.plot(n_values, n_log_n_complexity, label='O(n log n)', color='red')

# Adding titles and labels
plt.title('Time Complexity Comparison: O(n) vs O(n log n)')
plt.xlabel('Input Size (n)')
plt.ylabel('Time Complexity')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()



