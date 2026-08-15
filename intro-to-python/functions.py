# Define a function with parameters and a return statement.
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

# Call the function with different argument sets and print the results
print(f"\n--- calculate area ---")

print(calculate_area(5, 10))  

print(calculate_area(3, 7))   

print(calculate_area(8, 2))

# Create a reusable utility function
def format_name(first, last):
    """returns a formatted name by capitalizing the first and last names."""

    return f"{first.capitalize()} {last.capitalize()}"

# Call the utility function
print(f"\n--- format name ---")

print(format_name("dazai", "uchiha"))  

#  Grade calculator
def exam_grade(score, total):
    """Calculate the percentage score and return the grade."""
    
    #  Guard against invalid total marks and negative score
    try:
        if score < 0 or total <= 0:
            raise ValueError("Score and total must be positive numbers.")
        per = (score / total) * 100
        return round(per, 1)

    except (ValueError, ZeroDivisionError):
        return 0.0

# Call the Grade calculator function (including edge cases: 0, full marks, and a negative guard
print(f"\n--- exam grade ---")

print(f"full marks = {exam_grade(50, 50)}")
print(f"passed = {exam_grade(45, 50)}")
print(f"fail = {exam_grade(0, 50)}")
print(f"negative guard = {exam_grade(-10, 50)}")
