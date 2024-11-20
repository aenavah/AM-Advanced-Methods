import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Parameters
epsilon = 0.01  # Example value for epsilon
tau = 1  # Example value for tau, used in the approximation

# Define the differential equation for the numerical solution
def dydx(x, y):
    return (x**2 - 3*y) / (x + epsilon * y)

# Define the approximation function omega
def omega(t, tau):
    omega = (-12/(5*(t**7)-(4/5)*1/(t**2)+(t**3)/25) + 3/(t))*((5)/(2))
    return omega

# Define the range of x for the numerical solution
x_range = (1, 5)  # or any other range you want to explore
y_initial = [1]   # Initial condition: y(1) = 1

# Solve the differential equation numerically
solution = solve_ivp(dydx, x_range, y_initial, dense_output=True)

# Generate points to plot for the numerical solution
x_vals = np.linspace(1, 5, 100)
y_vals = solution.sol(x_vals)

# Define the range of t values for the approximation plot
t_values = np.linspace(0.1, 5, 100)  # Avoid t = 0 to prevent issues with t^t
omega_values = omega(t_values, tau)

# Plot both the numerical solution and the approximation
plt.figure(figsize=(12, 6))

# Plot the numerical solution
plt.subplot(1, 2, 1)
plt.plot(x_vals, y_vals[0], label=f'Numerical Solution for ε = {epsilon}')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Numerical Solution of the Differential Equation')
plt.legend()
plt.grid(True)

# Plot the approximation for omega
plt.subplot(1, 2, 2)
plt.plot(t_values, omega_values, label=r'$\omega = \frac{1}{2\tau^7} (15t^t - 12)$')
plt.xlabel('t')
plt.ylabel(r'$\omega(t)$')
plt.title('Plot of the Approximation for $\omega$')
plt.legend()
plt.grid(True)

# Show both plots
plt.tight_layout()
plt.show()
