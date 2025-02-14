'''
Inserting print() statements is a simple and effective way to debug the code
We can add print() statements at key points in the code to understand where things might be going wrong
'''

def divide(a, b):
    print(f"Dividing {a} by {b}")  # Debugging info
    return a / b

result = divide(10, 2)
print(f"Result: {result}")

# Debugging output:
# Dividing 10 by 2
# Result: 5.0

'''
VS Code
    - Set a breakpoint by clicking next to a line number.
    - Press F5 to start debugging.
    - Use Step Over (F10), Step Into (F11), Continue (F5).

PyCharm
    - Right-click the script and select "Debug".
    - Use Breakpoints and the Variables Window.
    - Step through code using F7 (Step Into), F8 (Step Over), F9 (Continue).


Basic profiling (finding performance issues):
    using cProfile (shows function execution times):
        python -m cProfile script.py

    using timeit for small code snippets (measures execution time of small code snippets):
        import timeit
        print(timeit.timeit("sum(range(1000))", number=10000))
'''