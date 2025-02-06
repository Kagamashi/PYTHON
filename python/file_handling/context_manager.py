''' Using with statement is the recommended way to work with files.
It ensures that the file is properly closed after its suite finishes.

With statement simplifies the code and makes it more readable by eliminating the need for explicitly closing the file using file.close() '''

# Using 'with' statement to read a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Using 'with' statement to write to a file
with open("example.txt", "w") as file:
    file.write("This is written using the 'with' statement.\n")
