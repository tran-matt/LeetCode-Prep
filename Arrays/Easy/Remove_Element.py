# 27. Remove Element
# Link: https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150

"""
Problem:
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed.
Then return the number of elements in nums which are not equal to val.

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100
"""
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k=0
        for num in nums:
            if num !=  val:
                nums[k] = num
                k += 1
        return k 
