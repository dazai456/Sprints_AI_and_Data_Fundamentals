#write a program that reads a score and prints “Pass”, “Merit”, or “Distinction”
print(f"\n--- If statements ---")

score = int(input("Enter your score: "))

if score >= 70:
    print("Distinction")
elif score >= 60:
    print("Merit")
else:
    print("Pass")

#add a condition using and / or / not
print(f"\n--- Logical operators ---")

attendance = float(input("Enter your attendance percentage: "))

if score >= 50 and attendance >= 80:
    print("You have passed.")
else:
    print("You have not passed.")

# Abracadabra: keep asking the user to guess a secret word
print(f"\n--- Abracadabra ---")

secret_word = "Abracadabra"
guess = ""
attempts = 0

while guess != secret_word:
    guess = input("Guess the secret word: ")
    attempts += 1

print(f"Congratulations! It took you {attempts} attempts to guess the secret word.")

# For loop: iterate over a word and replace every vowel with *
print(f"\n--- iterate over a word and replace every vowel with * ---")

word = input("Enter a word: ")
modified_word = ""

for char in word:
    if char.lower() in "aeiou":
        modified_word += "*"
    else:
        modified_word += char

print(f"Original word: {word}")

print(f"Modified word: {modified_word}")

# print a multiplication table (1–5 × 1–5)
print(f"\n--- print a multiplication table (1–5 × 1–5) ---")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()  # New line after each row