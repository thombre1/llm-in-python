def least_positive_index(arr):
    min_val = float('inf')
    min_index = -1
    
    for i, num in enumerate(arr):
        if num > 0 and num < min_val:
            min_val = num
            min_index = i
            
    return min_index

# Read input
arr = list(map(int, input().split()))

# Print the index of the smallest positive integer
print(least_positive_index(arr))