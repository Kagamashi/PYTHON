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
