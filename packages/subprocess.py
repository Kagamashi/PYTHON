'''
Running Shell Commands

executing shell commands from Python
'''

from subprocess import check_output, run

run(command, shell=True) # run shell command   
check_output(command)    # get output from a command

output = check_output(["echo", "Hello, world!"]).decode()
print(output)  # Output: Hello, world!
