import math
def f(x):
    """ Function to integrate, representing the upper half of a unit circle. """
    return math.sqrt(1 - x**2)

def riemann_sum(n):
    """ Computes the Riemann sum approximation for the area under the curve. """
    total_sum = 0
    delta_x = 1.0 / n
    
    for i in range(n):
        x_i = i * delta_x
        total_sum += f(x_i) * delta_x
    
    return total_sum

def approximate_pi(n):
    """ Approximates π using the Riemann sum approach with n subdivisions. """
    return 4 * riemann_sum(n)

# Example usage:
n = 10000  # Number of subdivisions
approximation = approximate_pi(n)
print(f"Approximation of π with {n} subdivisions: {approximation}")

