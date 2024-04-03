def find_max_recursive(S):
    n = len(S)
    # Base case
    if n == 1:
        return S[0]
    # Recursive step
    else:
        mid = n // 2
        max_left = find_max_recursive(S[:mid])
        max_right = find_max_recursive(S[mid:])
        # Compare and return the maximum element
        return max(max_left, max_right)

# Example usage:
sequence = [3, 7, 2, 8, 5, 9, 1, 4, 6]
print("Maximum element:", find_max_recursive(sequence))
