def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            left = mid + 1  # Search in the right half
        else:
            right = mid - 1  # Search in the left half

    return -1  # Not found

# Example usage:
arr = [2, 3, 5, 6, 8]  # Must be sorted
target = 6

result = binary_search(arr, target)
if result != -1:
    print(f"Binary Search: Found at index {result}")
else:
    print("Binary Search: Not found")
