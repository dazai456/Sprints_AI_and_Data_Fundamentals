# # a program that prints a solid arrow shape using * characters
arrow_width = 5

# Print the upper half of the arrow
for i in range(arrow_width):
    print("*" * (i + 1))

# Print the lower half of the arrow
for i in range(arrow_width - 2, -1, -1):
    print("*" * (i + 1))

