def find_min_max(sequence):
    # Base case:  
    if len(sequence) == 1:
        return sequence[0], sequence[0]
    
    # Recursive step:  
    mid = len(sequence) // 2
    left_min, left_max = find_min_max(sequence[:mid])
    right_min, right_max = find_min_max(sequence[mid:])
    
    # Combine the min and max values found in the two halves
    min_val = min(left_min, right_min)
    max_val = max(left_max, right_max)
    
    return min_val, max_val

# Example usage:
sequence = [3, 7, 2, 8, 5, 9, 1, 4, 6]
min_val, max_val = find_min_max(sequence)
print("Minimum value:", min_val)
print("Maximum value:", max_val)
