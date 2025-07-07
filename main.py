import numpy as np
import matplotlib.pyplot as plt
from AlphaFractal import AlphaFractal

# Define the interval and partition
I = [0, np.pi]  # Interval for sine function
N = 5  # Number of intervals
max_depth = 7  # Set max depth for fractal generation

# Original function f(x)
def f(x):
    return np.sin(x)

# Base function b(x)
def b(x):
    return np.cos(2 * x) * f(x)

# Define an array for alpha values, each corresponding to one transformation
alpha_array = [0.5, -0.5, 0.5, -0.5, 0.5]  # Adjust values as needed

# Initialize the AlphaFractal with the array of alpha values and transformations
alpha_fractal = AlphaFractal(scale_vector=alpha_array, b_func=b, f_func=f, interval=I, num_intervals=N, max_depth=max_depth)

# Generate fractal points using the generate_points method
x_vals, y_vals = alpha_fractal.generate_points(0.5, 0.5)  # Starting point

# Generate x values for plotting the original sine function
x_values = np.linspace(I[0], I[1], 500)
f_values = f(x_values)

# Create the plots
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Plot (a): Original function sin(x)
ax[0].plot(x_values, f_values, label='Function $f(x)$', color='black')
ax[0].set_title('Original function $f(x)$')
ax[0].legend()
ax[0].grid()

# Plot (b): Fractal function points
ax[1].scatter(x_vals, y_vals, label='Fractal function $f^{{\\alpha}}(x)$', color='black', marker='.', s=0.0001)
ax[1].set_title('Fractal function $f^{\\alpha}(x)$')
ax[1].set_xlim(I[0], I[1])
ax[1].set_ylim(-6, 8)
ax[1].legend()
ax[1].grid()

plt.tight_layout()
plt.show()
