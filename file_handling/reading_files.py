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
