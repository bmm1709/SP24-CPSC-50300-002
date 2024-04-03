import time
import random
import matplotlib.pyplot as plt

def test_sorted_time(n):
    lst = [random.randint(1, 1000) for _ in range(n)]  # Generate a list of size n with random elements
    start_time = time.time()
    sorted_lst = sorted(lst)  # Sort the list using Python's sorted() method
    end_time = time.time()
    return end_time - start_time

# Test sorting time for different problem sizes
problem_sizes = [1000, 2000, 3000, 4000, 5000]
execution_times = []

for size in problem_sizes:
    execution_time = test_sorted_time(size)
    execution_times.append(execution_time)
    print(f"Problem size: {size}, Execution time: {execution_time:.6f} seconds")

# Plot the results
plt.plot(problem_sizes, execution_times, marker='o')
plt.xlabel('Problem Size (n)')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of Python\'s sorted() Method')
plt.grid(True)
plt.show()