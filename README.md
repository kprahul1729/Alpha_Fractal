## AlphaFractal

A Python class for generating and visualizing alpha-fractal functions using iterated function systems (IFS) on intervals partitioned into equal subintervals. This is useful for research and education in fractal interpolation, self-similar structures, and mathematical visualization.

# Features

* Customizable scaling: User-defined alpha (scaling) values per subinterval.

* Flexible functions: Accepts any base and target functions.

* Configurable partitioning: Choose interval, number of subintervals, and recursion depth.

* Automated transformation: Dynamically creates transformation functions for each subinterval.

* Easy plotting: Generates point sets for easy visualization.

# Requirements

- numpy

- matplotlib

# Usage
<pre>``` AlphaFractal(scale_vector, b_func, f_func, interval, num_intervals, max_depth) ```<pre>

* scale_vector: * List/array of alpha (scaling) values, length = num_intervals

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
