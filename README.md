#AlphaFractal

A Python class for generating and visualizing alpha-fractal functions using iterated function systems (IFS) on intervals partitioned into equal subintervals. This is useful for research and education in fractal interpolation, self-similar structures, and mathematical visualization.

Features
Customizable scaling: User-defined alpha (scaling) values per subinterval.

Flexible functions: Accepts any base and target functions.

Configurable partitioning: Choose interval, number of subintervals, and recursion depth.

Automated transformation: Dynamically creates transformation functions for each subinterval.

Easy plotting: Generates point sets for easy visualization.

Requirements
numpy

matplotlib

Usage
1. Import and Define Functions
python
import numpy as np
import matplotlib.pyplot as plt

def b_func(x):
    return np.sin(x)

def f_func(x):
    return np.cos(x)
2. Initialize the Fractal
python
interval = (0, np.pi)
num_intervals = 4
scale_vector = [0.5, 0.6, 0.7, 0.8]
max_depth = 5

fractal = AlphaFractal(
    scale_vector=scale_vector,
    b_func=b_func,
    f_func=f_func,
    interval=interval,
    num_intervals=num_intervals,
    max_depth=max_depth
)
3. Generate and Plot Points
python
x0, y0 = interval[0], b_func(interval[0])
points_x, points_y = fractal.generate_points(x0, y0)

plt.scatter(points_x, points_y, s=1)
plt.title("Alpha Fractal")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
Class Reference
AlphaFractal
Constructor:

python
AlphaFractal(scale_vector, b_func, f_func, interval, num_intervals, max_depth)
scale_vector: List/array of alpha (scaling) values, length = num_intervals

b_func: Base function, e.g., lambda x: ...

f_func: Target function, e.g., lambda x: ...

interval: Tuple (start, end)

num_intervals: Number of equal subintervals

max_depth: Recursion depth

Methods:

generate_points(x0, y0): Returns lists of x and y coordinates for the fractal, starting at (x0, y0).

Notes
Designed for intervals divided into equal subintervals.

The choice of scale_vector, b_func, and f_func affects the fractal's shape and properties.

Higher max_depth yields more detail but increases computation time and memory usage.
