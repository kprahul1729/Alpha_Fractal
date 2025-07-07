class AlphaFractal: # only for subintervals with equal size
    def __init__(self, scale_vector, b_func, f_func, interval, num_intervals, max_depth):
        self.scale_vector = scale_vector    # Define alpha  values as a class member
        self.b_func = b_func  # Define Base function as a class member
        self.f_func = f_func  # Define function  as a class member
        self.I = interval  # Define interval as a class member
        self.N = num_intervals  # Define the number of intervals as a class member
        self.max_depth = max_depth  # Define max_depth as a class member
        self.h = (self.I[1] - self.I[0]) / self.N  # Calculate partition width
        self.transformations = []     # for storing w_i (x,y)
        self.create_transformations()   # making w_i(x,y)

    def create_transformations(self):
        for i in range(self.N):
            alpha = self.scale_vector[i]

            # Define L_i function for current i and add it to transformations
            def L_i(x, i=i):  # Capture current i in the function
                return (x - self.I[0]) / self.N + self.I[0] + i * self.h

            def w(x, y, alpha=alpha, L_i=L_i):
                x_new = L_i(x)
                y_new = alpha * (y - self.b_func(x)) + self.f_func(x_new)
                return x_new, y_new

            self.transformations.append(w)
    # Generating points for ploting Alpha Fractral
    def generate_points(self, x0, y0):
        current_points = [(x0, y0)]
        points_x, points_y = [x0], [y0]

        for depth in range(self.max_depth):
            new_points = []
            for (x, y) in current_points:
                for transform in self.transformations:# taking each w_i(x,y) one by one
                    new_x, new_y = transform(x, y)
                    points_x.append(new_x)
                    points_y.append(new_y)
                    new_points.append((new_x, new_y))
            current_points = new_points

        return points_x, points_y  # Return generated points
