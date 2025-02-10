'''
Ordered collection of objects

- differs from lists in the way that they store elements in memory
    (lists use a contiguous memory block to store references to their data)
- each elements of a linked list is called a node, and every node has two fields:
    data: contains value to be stored in the data
    next: contains a reference to the next node on the list
- first node is called head, and last node must have it's next reference pointing to None

practical applications:
-   queues (FIFO) or stacks (LIFO)
-   graphs: for example adjacency list to show relationship between objects in directed acyclic graph (DAG)


'''