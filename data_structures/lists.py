'''
List is an ordered, mutable collection of items.
List allows duplicates and can contain elements of different data types.
Lists support methods:
  append(item): Adds an item to the end.
  pop(): Removes and returns the last item.
  extend([items]): Adds all items from another list.
  remove(item): Removes the first occurrence of the specified item.
  sort(): Sorts the list in place.
  reverse(): Reverses the list in place.
'''

my_list = [1, 2, 3]
my_list.append(4)  # Adds 4 to the list
print(my_list)  # Output: [1, 2, 3, 4]

my_list.pop()  # Removes the last element (4)
print(my_list)  # Output: [1, 2, 3]

my_list.extend([5, 6])  # Extends the list
print(my_list)  # Output: [1, 2, 3, 5, 6]
