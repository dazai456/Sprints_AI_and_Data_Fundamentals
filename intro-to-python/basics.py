import datetime
 
#  input name and age from user
name = input('enter your name: ')
age = input('enter your age: ')

# create a string using concatenation
print(f"\n--- create a string using concatenation ---")
str_1 = 'Hello, ' + name + '! You are ' + age + ' years old.'

print(str_1)

# calculate the birth year based on the current year and age
current_year = datetime.datetime.now().year

try:
    age = int(age)
    
    if age < 0:
        print('Age cannot be negative. Please enter a valid age.')
    
    birth_year = current_year - age
    print('You were born in ' + str(birth_year) + '.')

except (ValueError, TypeError):
    print('Invalid age input. Please enter a valid number for age.')
    
# demonstrate string methods
print(f"\n--- string methods ---")

print(str_1.upper())

print(str_1.lower())

print(str_1.strip())

print(str_1.replace('Hello', 'Hi buddy'))

print(str_1.find('years'))

# demonstrate slicing
print(f"\n--- demonstrate slicing ---")

print(str_1[0:5])

print(str_1[-5:])

print(str_1[::2])

print(str_1[::-1])

# Formatted strings
print(f"\n--- Formatted strings ---")

print(f'Hello, {name}! You are {age} years old.');  print('Hello, {name}! You are {age} years old.'.format(name="name", age="age"))