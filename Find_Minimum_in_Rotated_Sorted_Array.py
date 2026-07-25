"""
LeetCode 153 - Find Minimum in Rotated Sorted Array

Problem:
---------
Given a rotated sorted array of unique elements, find the minimum element.

Example:
nums = [4,5,6,7,0,1,2]

The original sorted array was:
[0,1,2,4,5,6,7]

After rotation, the smallest element is 0.


Approach:
---------
We use Binary Search.

A rotated sorted array contains two sorted parts.
The minimum element is the point where the rotation happens.

At every step:
1. Check if the current range is already sorted.
   If it is, nums[left] is the smallest element in this range.

2. Otherwise, find the middle element:
   - If nums[mid] >= nums[left], then the left half is sorted.
     The minimum must be in the right half.
   - Otherwise, the rotation point is in the left half.


Complexity Analysis:
--------------------
Time Complexity:
    O(log n)

    Binary search eliminates half of the search space
    in every iteration.

Space Complexity:
    O(1)

    Only constant extra variables are used.
"""


from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:

        # Store the smallest value found so far.
        # Initialize with the first element.
        res = nums[0]

        # Binary search pointers
        left = 0
        right = len(nums) - 1


        while left <= right:

            # If the current portion is already sorted,
            # then nums[left] is the minimum element
            # in this range.
            #
            # Example:
            # [1,2,3,4]
            #
            # No rotation exists in this range.
            if nums[left] < nums[right]:
                res = min(res, nums[left])
                break


            # Find the middle index
            mid = (left + right) // 2


            # Update the minimum value
            # with the middle element.
            res = min(res, nums[mid])


            # If the left half is sorted:
            #
            # Example:
            # [4,5,6,7,0,1,2]
            #       ^
            #       mid
            #
            # The minimum cannot be in the left sorted part,
            # so search in the right half.
            if nums[mid] >= nums[left]:
                left = mid + 1


            # Otherwise, the rotation point is in the left half.
            else:
                right = mid - 1


        return res



# -----------------------------
# Testing the solution locally
# -----------------------------

if __name__ == "__main__":

    solution = Solution()

    nums = [4, 5, 6, 7, 0, 1, 2]

    result = solution.findMin(nums)

    print("Input:", nums)
    print("Minimum element:", result)