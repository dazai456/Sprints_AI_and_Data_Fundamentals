try:
    f = open("output.txt", "w")

    f.write("Hello, World!")
    
    f.close()

except PermissionError:
    print("Permission denied")

except IOError:
    print("I/O error occurred")