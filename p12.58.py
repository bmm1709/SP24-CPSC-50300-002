import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index, right_index = 0, 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def generate_random_sequence(size):
    return [random.randint(0, 1000) for _ in range(size)]

def generate_almost_sorted_sequence(size, shuffle_percent):
    sequence = list(range(size))
    shuffle_size = int(size * shuffle_percent)
    shuffle_indices = random.sample(range(size), shuffle_size)
    for i in shuffle_indices:
        j = random.randint(0, size - 1)
        sequence[i], sequence[j] = sequence[j], sequence[i]
    return sequence

def benchmark_sorting_algorithm(algorithm, dataset):
    start_time = time.time()
    algorithm(dataset)
    end_time = time.time()
    return end_time - start_time

# Test dataset generation
random_sequence = generate_random_sequence(1000)
almost_sorted_sequence = generate_almost_sorted_sequence(1000, 0.1)

# Benchmarking
merge_sort_time_random = benchmark_sorting_algorithm(merge_sort, random_sequence.copy())
quick_sort_time_random = benchmark_sorting_algorithm(quick_sort, random_sequence.copy())

merge_sort_time_almost_sorted = benchmark_sorting_algorithm(merge_sort, almost_sorted_sequence.copy())
quick_sort_time_almost_sorted = benchmark_sorting_algorithm(quick_sort, almost_sorted_sequence.copy())

# Print results
print("Random Sequence:")
print("Merge Sort Time:", merge_sort_time_random)
print("Quick Sort Time:", quick_sort_time_random)

print("\nAlmost Sorted Sequence:")
print("Merge Sort Time:", merge_sort_time_almost_sorted)
print("Quick Sort Time:", quick_sort_time_almost_sorted)
