def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index where the target is found
    return -1  # Return -1 if not found

# Example usage:
arr = [5, 3, 8, 6, 2]
target = 6

result = linear_search(arr, target)
if result != -1:
    print(f"Linear Search: Found at index {result}")
else:
    print("Linear Search: Not found")
