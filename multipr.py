
import math
import multiprocessing

def f(x):
    """ Function to integrate, representing the upper half of a unit circle. """
    return math.sqrt(1 - x**2)

def partial_riemann_sum(start, end, delta_x):
    """ Computes a partial Riemann sum for the given range. """
    total_sum = 0
    x_i = start
    try:
        while x_i < end:
            total_sum += f(x_i) * delta_x
            x_i += delta_x
    except Exception as e:
        print(f"Error in partial_riemann_sum: {e}")
    return total_sum

def approximate_pi(n, num_processes):
    """ Approximates π using Riemann sums with multiprocessing. """
    delta_x = 1.0 / n
    chunk_size = n // num_processes
    
    # Adjust chunk size for even distribution of workload
    chunk_size = max(chunk_size, 1)
    
    # Creating a pool of processes
    pool = multiprocessing.Pool(processes=num_processes)
    
    # Calculate the start and end points for each process
    ranges = [(i * chunk_size * delta_x, (i + 1) * chunk_size * delta_x) for i in range(num_processes)]
    
    # Distribute the work using map
    results = pool.starmap(partial_riemann_sum, [(start, end, delta_x) for start, end in ranges])
    
    # Wait for all processes to complete and sum the results
    total_sum = sum(results)
    
    pool.close()
    pool.join()
    
    return 4 * total_sum

# Example usage:
if __name__ == '__main__':
    n = 10000  # Number of subdivisions
    num_processes = 6  # Number of processes
    approximation = approximate_pi(n, num_processes)
    print(f"Approximation of π with {n} subdivisions and {num_processes} processes: {approximation}")
