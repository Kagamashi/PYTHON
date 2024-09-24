'''
Multiprocessing allows to create separate processes, each with its own memory space, enabling true parallelism.
Useful for CPU-bound tasks.
Python multiprocessing module provides support for creating and managing processes:
  Creating a process: You can create a new process by instantiating the Process class from the multiprocessing module.
  Starting a process: Use the start() method to start the process.
  Joining a process: Use the join() method to wait for the process to complete.

Each process runs independently with its own memory space.
Multiprocessing can bypass the Global Interpreter Lock (GIL) and is ideal for CPU-bound tasks that require true parallel execution.
Shared memory or message passing (using Queue or Pipe) can be used for communication between processes.
'''

import multiprocessing
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

if __name__ == "__main__":
    # Creating processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_numbers)

    # Starting processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Both processes finished execution")
