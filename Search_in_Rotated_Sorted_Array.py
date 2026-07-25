"""
LeetCode 33 - Search in Rotated Sorted Array

Problem:
---------
Given a rotated sorted array of unique integers and a target value,
return the index of the target if it exists, otherwise return -1.

Example:

Input:
nums = [4,5,6,7,0,1,2]
target = 0

Output:
4


Approach:
---------
Modified Binary Search

A rotated sorted array consists of two sorted parts.

Example:
nums = [4,5,6,7,0,1,2]

Left sorted part:
[4,5,6,7]

Right sorted part:
[0,1,2]


At every step of binary search:

1. Find the middle element.
2. If nums[mid] is the target, return mid.
3. Determine which half of the array is sorted:
   
   - If nums[left] <= nums[mid]:
        The left half is sorted.
        Check if target exists in this range.
        If yes, search left side.
        Otherwise, search right side.

   - Otherwise:
        The right half is sorted.
        Check if target exists in this range.
        If yes, search right side.
        Otherwise, search left side.


Why this works:
---------------
In a rotated sorted array, at least one half of the array
will always remain sorted.

By identifying the sorted half, we can eliminate half of the
search space in every iteration.


Complexity Analysis:
--------------------
Time Complexity:
    O(log n)

    Binary search reduces the search space by half each iteration.

Space Complexity:
    O(1)

    Only constant extra variables are used.
"""


from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1


        while left <= right:

            # Find middle element
            middle = (left + right) // 2


            # Target found
            if nums[middle] == target:
                return middle


            # Check if left half is sorted
            if nums[left] <= nums[middle]:

                # Target is outside the sorted left half,
                # so search the right half
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1

                # Target exists inside the left sorted half
                else:
                    right = middle - 1


            # Right half is sorted
            else:

                # Target is outside the sorted right half,
                # so search the left half
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1

                # Target exists inside the right sorted half
                else:
                    left = middle + 1


        # Target does not exist
        return -1



# -----------------------------
# Testing the solution locally
# -----------------------------

if __name__ == "__main__":

    solution = Solution()


    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    result = solution.search(nums, target)


    print("Array:", nums)
    print("Target:", target)
    print("Index:", result)