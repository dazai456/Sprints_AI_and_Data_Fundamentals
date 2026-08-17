try:
    f = open("input.txt", "r")\
    
except FileNotFoundError:
    print("File not found")