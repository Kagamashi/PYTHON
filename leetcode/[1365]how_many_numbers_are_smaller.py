'''
[ARRAY]
Given an array nums for each nums[i] find out how many numbers in the array are smaller than it.
For each nums[i] count the number of valid j's such that j != i and nums[j] < nums[i]

Input: nums = [8, 1, 2, 2, 3]
Output: [4, 0, 1, 1, 3]
'''

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        