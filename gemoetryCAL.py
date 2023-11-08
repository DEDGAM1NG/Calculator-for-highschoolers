import math
import tkinter as tk

def quadratic_solver():
    a = float(a_entry.get())
    b = float(b_entry.get())
    c = float(c_entry.get())
    
    discriminant = (b**2) - 4*a*c
    
    if discriminant < 0:
        result_label.config(text="No real solutions exist.")
    else:
        square_root_part = math.sqrt(discriminant)
        first_solution = (-b + square_root_part) / (2*a)
        second_solution = (-b - square_root_part) / (2*a)
        result_label.config(text=f"The solutions are {first_solution} and {second_solution}")

def distance_and_midpoint_calculator():
    x1 = float(x1_entry.get())
    y1 = float(y1_entry.get())
    x2 = float(x2_entry.get())
    y2 = float(y2_entry.get())
    
    distance_variable_x = (x2 - x1)**2
    distance_variable_y = (y2 - y1)**2
    distance_variable_xy = distance_variable_x + distance_variable_y
    midpoint_variable_x = ((x1 + x2) / 2)
    midpoint_variable_y = ((y1 + y2) / 2)
    
    distance_answer = math.sqrt(distance_variable_xy)
    result_label.config(text=f"The distance is {distance_answer} or sqrt of ({distance_variable_xy})")
    midpoint_label.config(text=f"Midpoint is {midpoint_variable_x}, {midpoint_variable_y}")

def linear_equation_solver():
    slope = float(slope_entry.get())
    point_x = float(point_x_entry.get())
    point_y = float(point_y_entry.get())
    y_intercept_step1 = slope * point_x
    y_intercept = point_y - y_intercept_step1
    
    result_label.config(text=f"The equation of the line is y = {slope}x + {y_intercept}")

root = tk.Tk()
root.title("Calculator with GUI")

# Create input fields and labels
a_label = tk.Label(root, text="Enter A:")
a_label.pack()
a_entry = tk.Entry(root)
a_entry.pack()

b_label = tk.Label(root, text="Enter B:")
b_label.pack()
b_entry = tk.Entry(root)
b_entry.pack()

c_label = tk.Label(root, text="Enter C:")
c_label.pack()
c_entry = tk.Entry(root)
c_entry.pack()

x1_label = tk.Label(root, text="Enter x1:")
x1_label.pack()
x1_entry = tk.Entry(root)
x1_entry.pack()

y1_label = tk.Label(root, text="Enter y1:")
y1_label.pack()
y1_entry = tk.Entry(root)
y1_entry.pack()

x2_label = tk.Label(root, text="Enter x2:")
x2_label.pack()
x2_entry = tk.Entry(root)
x2_entry.pack()

y2_label = tk.Label(root, text="Enter y2:")
y2_label.pack()
y2_entry = tk.Entry(root)
y2_entry.pack()

slope_label = tk.Label(root, text="Enter slope (m):")
slope_label.pack()
slope_entry = tk.Entry(root)
slope_entry.pack()

point_x_label = tk.Label(root, text="Enter point's x-coordinate:")
point_x_label.pack()
point_x_entry = tk.Entry(root)
point_x_entry.pack()

point_y_label = tk.Label(root, text="Enter point's y-coordinate:")
point_y_label.pack()
point_y_entry = tk.Entry(root)
point_y_entry.pack()

# Create buttons to trigger calculations
quadratic_button = tk.Button(root, text="Solve Quadratic Equation", command=quadratic_solver)
quadratic_button.pack()

distance_midpoint_button = tk.Button(root, text="Calculate Distance and Midpoint", command=distance_and_midpoint_calculator)
distance_midpoint_button.pack()

linear_equation_button = tk.Button(root, text="Solve Linear Equation", command=linear_equation_solver)
linear_equation_button.pack()

# Create a label to display results
result_label = tk.Label(root, text="")
result_label.pack()

midpoint_label = tk.Label(root, text="")
midpoint_label.pack()

root.mainloop()
