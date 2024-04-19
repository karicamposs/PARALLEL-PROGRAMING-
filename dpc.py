from mpi4py import MPI
import math
def f(x):
    """ Function to integrate, representing the upper half of a unit circle. """
    return math.sqrt(1 - x**2)

def compute_segment(start, end, delta_x):
    """ Computes the Riemann sum for a segment of the integration interval. """
    total_sum = 0
    x_i = start
    while x_i < end:
        total_sum += f(x_i) * delta_x
        x_i += delta_x
    return total_sum

def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    n = 10000  # Total number of subdivisions
    delta_x = 1.0 / n

    # Determine the portion of the interval each process will handle
    chunk_size = n // size
    start = rank * chunk_size * delta_x
    end = start + chunk_size * delta_x

    # Handle the last process to take any remaining subdivisions
    if rank == size - 1:
        end = 1.0

    local_sum = compute_segment(start, end, delta_x)

    # Gather all the local sums at the root process
    total_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

    # Calculate and print π approximation at the root
    if rank == 0:
        pi_approx = 4 * total_sum
        print(f"Approximation of π with {n} subdivisions across {size} processes: {pi_approx}")

if __name__ == '__main__':
    main()
