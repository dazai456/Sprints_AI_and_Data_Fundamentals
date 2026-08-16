# Custom exception for invalid age
class AgeError(Exception):
    pass

# Main program
try:
    age = int(input("Enter your age: "))

    # Validate age
    if age < 0 or age > 120:
        raise AgeError("Error: Age must be between 0 and 120.")
    
    # If age is valid, print it
    print(f"Your age is: {age}")
    
except ValueError: # Handle non-integer input
    print("Invalid input. Please enter a valid integer for age. between 0 and 120.")

except AgeError as e: # Handle custom age error
    print(e)