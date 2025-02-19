
'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# Approach 1: Brute force - high time complexity O(n^2)
# consider every pair of elements and check if their sum equals the target

# List[int] - list containing integers
# -> List[int] - indicates twoSum will return a list of integers
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range (n-1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
            
        return []



## Approach 2: Two-pass Hash Table
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        n = len(nums)

        # build hash table
        for i in range(n):
            hashTable[nums[i]] = i