import math

# Write expressions using all arithmetic operators: + - * / // % ** —
print(f"\n--- using all arithmetic operators ---")
x = 10
y = 12

print("Addition:", x + y)

print("Subtraction:", x - y)

print("Multiplication:", x * y)

print("Division:", x / y)

print("Floor Division:", x // y)

print("Modulus:", x % y)

print("Exponentiation:", x ** y)

# Demonstrate operator precedence
print(f"\n--- operator precedence ---")

print("Operator Precedence:", x + y * 2)

print("Operator Precedence with Parentheses:", (x + y) * 2)

print("Operator Precedence with Exponentiation:", x ** y + 2)


# Use the math module to calculates the area and circumference of a circle given a radius from input().
radius = int(input("Enter the radius of a circle: "))

area = math.pi * math.pow(radius, 2)

radius_from_sqrt = math.sqrt(math.pow(radius, 2))

circumference = 2 * math.pi * radius_from_sqrt

# exact calculations
print(f"\n--- Precise Calculations ---")

print(f"Exact Area: {area}")

print(f"Exact Circumference: {circumference}")

# show rounded integer bounds
print(f"\n--- Rounded Bounds ---")

print(f"Area (Ceiling): {math.ceil(area)}")

print(f"Area (Floor): {math.floor(area)}")

print(f"Circumference (Ceiling): {math.ceil(circumference)}")

print(f"Circumference (Floor): {math.floor(circumference)}")
