'''


'''


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




''' open() functions is used to open a file
We must specify the file name and mode in which the file should be opened:
'r': Read (default) – Opens a file for reading. If the file does not exist, it raises an error.
'w': Write – Opens a file for writing. If the file does not exist, it creates a new one. If the file exists, it truncates (overwrites) the content.
'a': Append – Opens a file for appending. If the file does not exist, it creates a new one. If the file exists, new data is added to the end.
'r+': Read and Write – Opens a file for both reading and writing. The file must exist.
'''

# Opening a file in read mode
file = open("example.txt", "r")

# Opening a file in write mode (overwrites the file if it exists)
file = open("example.txt", "w")

# Opening a file in append mode (appends to the file)
file = open("example.txt", "a")




''' Once file is opened we can read its contents using one of the following methods:
read(): Reads the entire content of the file as a single string.
readline(): Reads one line at a time from the file.
readlines(): Reads all lines of the file and returns them as a list of strings.
'''

# Reading the entire content of the file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Reading the file line by line using readline()
file = open("example.txt", "r")
line = file.readline()  # Reads the first line
print(line)
file.close()

# Reading all lines into a list using readlines()
file = open("example.txt", "r")
lines = file.readlines()  # Returns a list of all lines
print(lines)
file.close()




''' To write data to a file:
write(): Writes a single string to the file. You need to manually add newline characters (\n) if you want to separate lines.
writelines(): Writes a list of strings to the file. Each string in the list is written as a line, but newline characters must be included in the strings.
'''

# Writing a single line to the file
file = open("example.txt", "w")
file.write("This is a new line.\n")  # Remember to add '\n' for a new line
file.close()

# Writing multiple lines using writelines()
file = open("example.txt", "w")
lines = ["First line\n", "Second line\n", "Third line\n"]
file.writelines(lines)
file.close()





