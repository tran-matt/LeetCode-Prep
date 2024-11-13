# 88. Merge Sorted Array
# Link: https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

"""
Problem:
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should be stored inside the array nums1.

Constraints:
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

Follow-up: Can you come up with an algorithm that runs in O(m + n) time?

Solution:
This solution combines the first m elements of nums1 with all elements of nums2,
then sorts the resulting array in place. 
"""

def merge_simple(nums1, m, nums2, n):
    # Combine the first m elements of nums1 with all elements of nums2
    nums1[:m + n] = sorted(nums1[:m] + nums2)