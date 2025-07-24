def min_operations_to_palindrome(arr):
    n = len(arr)
    operations = 0
    
    L, R = 0, n - 1
    
    # Use two pointers approach to make the array palindromic
    while L < R:
        if arr[L] < arr[R]:
            operations += arr[R] - arr[L]
            arr[L] = arr[R]
        elif arr[L] > arr[R]:
            operations += arr[L] - arr[R]
            arr[R] = arr[L]
        L += 1
        R -= 1
    
    return operations

# Example Input 1
arr1 = [2, 6, 4, 3, 4,1]
print(min_operations_to_palindrome(arr1))  

# Example Input 2
arr2 = [1, 2, 3, 3, 4, 3, 2, 1]
print(min_operations_to_palindrome(arr2))
