try :
    with open("input.txt", 'r') as f:
        
        content = f.read()
        
        content = content.swapcase()
        
        print(content)

except FileNotFoundError:

    print("File not found")

# Write the modified content to a new file
with open("modified.txt","w") as f:
    f.write(content)