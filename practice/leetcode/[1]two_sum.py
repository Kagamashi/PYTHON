
'''
Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''

# List[int] - list containing integers
# -> List[int] - indicates twoSum will return a list of integers


## Approach 1: Two-pass Hash Table - O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        n = len(nums)

        # build hash table
        for i in range(n):
            hashTable[nums[i]] = i

        # find the complement
        for i in range(n):
            complement = target - nums[i]
            if complement in hashTable and hashTable[complement] != i:
                return [i, hashTable[complement]]
        
        return []


# Approach 2: One-pass Hash Table - O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in hashTable:
                return [hashTable[complement], i]
            hashTable[nums[i]] = i

        return []
