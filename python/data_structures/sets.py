'''
Set is unordered, collection of unique items.
Sets do not allow duplicates and are useful for operations like union, intersection and difference.
Methods:
  add(item): Adds an item to the set.
  remove(item): Removes an item (raises an error if it doesn’t exist).
  union(): Returns a new set with all items from both sets.
  intersection(): Returns a set with only the items present in both sets.
  difference(): Returns a set with items present in the first set but not in the second.
'''

my_set = {1, 2, 3}
my_set.add(4)  # Adds 4 to the set
print(my_set)  # Output: {1, 2, 3, 4}

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a.union(set_b))  # Output: {1, 2, 3, 4, 5}
print(set_a.intersection(set_b))  # Output: {3}
