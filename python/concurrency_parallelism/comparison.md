| Feature              | Multithreading                 | Multiprocessing                | Asynchronous Programming      |
|----------------------|--------------------------------|--------------------------------|-------------------------------|
| **Concurrency Type**  | Threads (shared memory)        | Processes (separate memory)    | Coroutines (non-blocking I/O) |
| **Parallel Execution**| Limited by GIL                | True parallelism               | Not parallel, but non-blocking|
| **Best For**          | I/O-bound tasks               | CPU-bound tasks                | I/O-bound tasks               |
| **Use Case**          | Network requests, file I/O    | Heavy computations             | Web scraping, network I/O     |
