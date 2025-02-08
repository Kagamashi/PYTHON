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
