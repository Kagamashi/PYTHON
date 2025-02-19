'''
Two Pointer Technique is an efficient algorithmic approach used for solving array and string problems by using two indices (pointers) that traverse the structure in specific way

+ used for searching, sorting, and optimization problems
+ reduces time complexity from O(n²) to O(n) or O(log n)
+ common in problems involving sorted arrays, subarrays, linked lists

types of Two Pointer approach:
    opposite direction (left-right) : one pointer starts from the left, the other from the right
        finding pairs, palindromes, sorting
    same direction (sliding window) : both pointers move in the same direction
        subarrays, searching, string problems
    fast-slow (tortoise & hare) : one pointer moves faster than the other
        linked list cycle detection
'''

''' Opposite Direction
    - Used for finding pairs with a given sum in a sorted array.
    ✅ More efficient (O(n)) than brute-force (O(n²)) since each element is checked at most once '''
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1  # Two pointers

    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return [left, right]  # Found the pair
        
        if current_sum < target:
            left += 1  # Move left pointer to increase sum
        else:
            right -= 1  # Move right pointer to decrease sum

    return []  # No pair found

arr = [1, 2, 3, 4, 6, 8, 9]
target = 10
print(two_sum_sorted(arr, target))  # Output: [1, 4] (2 + 8 = 10)


''' Same Direction
    - Used when processing contiguous subarrays or substrings
    ✅ Time Complexity: O(n), since each character is processed at most twice.
'''
def longest_unique_substring(s):
    seen = set()  # Track characters
    left = 0
    max_length = 0
    
    for right in range(len(s)):  # Right pointer expands the window
        while s[right] in seen:  # Shrink from the left if duplicate found
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

s = "abcabcbb"
print(longest_unique_substring(s))  # Output: 3 ("abc")


''' Fast-Slow Pointers
    - Used for cycle detection in linked lists (O(n)).
    - Also known as Floyd’s Tortoise and Hare Algorithm.
    ✅ Time Complexity: O(n), as each node is visited at most once. '''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow, fast = head, head  # Two pointers

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next  # Fast pointer moves twice as fast

        if slow == fast:
            return True  # Cycle detected
    
    return False  # No cycle

# Example usage:
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node1  # Cycle

print(has_cycle(node1))  # Output: True
