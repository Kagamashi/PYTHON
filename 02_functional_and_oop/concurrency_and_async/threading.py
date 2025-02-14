'''
[ concurrency, not true parallelism]

Multithreading allows to run multiple threads (smaller units of a process) concurrently within a single process
Python threading module provides a simple way to work with threads
  Creating a thread: You can create a new thread by instantiating the Thread class from the threading module and passing it a target function.
  Starting a thread: Use the start() method to start the thread.
  Joining a thread: Use the join() method to wait for the thread to complete

Threads run concurrently and share the same memory space.
The Global Interpreter Lock (GIL) limits true parallel execution in CPU-bound tasks but can be useful for I/O-bound tasks like file I/O or network requests.
'''

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

# Creating threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_numbers)

# Starting threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads finished execution")
