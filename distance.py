import math

# ------------------------------------------
# Collect Coordinates From The User
# ------------------------------------------
# We use floating-point numbers to allow decimal inputs for accuracy.
start_x = float(input("Enter x1: "))
start_y = float(input("Enter y1: "))
end_x   = float(input("Enter x2: "))
end_y   = float(input("Enter y2: "))

# ------------------------------------------
# Calculate Distance Using Mathematical Functions
# ------------------------------------------
# We separate the differences to make the formula easier to read.
x_difference_squared = math.pow(end_x - start_x, 2)
y_difference_squared = math.pow(end_y - start_y, 2)

# Combine the squared values and calculate the final square root
total_distance = math.sqrt(x_difference_squared + y_difference_squared)

# ------------------------------------------
# Output The Verified Results
# ------------------------------------------
# The result is formatted using an f-string to show exactly 2 decimal places.
print(f"The distance between the two points is: {total_distance:.2f}")
