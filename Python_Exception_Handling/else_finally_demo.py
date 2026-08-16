x  = int(input("Enter a number: "))

y = int(input("Enter another number: "))

print("Connecting…")

try:
    # Perform division operation
    result = x / y

except ZeroDivisionError:

    print("Error: Division by zero is not allowed.")

else:

    print("Operation succeeded.")

finally:

    print("Cleaning up…")