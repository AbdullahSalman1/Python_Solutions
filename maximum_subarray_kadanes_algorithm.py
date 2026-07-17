"""
===============================================================================
                 Maximum Subarray (LeetCode 53)
                    Kadane's Algorithm
===============================================================================

Problem:
--------
Given an integer array nums, find the contiguous subarray that has the largest
sum and return that sum.

A subarray must contain consecutive elements.


Example:
--------
Input:
nums = [-2,1,-3,4,-1,2,1,-5,4]

Output:
6

Explanation:
The subarray [4,-1,2,1] has the largest sum.

4 + (-1) + 2 + 1 = 6


===============================================================================
Approach: Kadane's Algorithm
===============================================================================

Intuition:
----------
While iterating through the array, we maintain the sum of the current subarray.

If the current sum becomes negative:
    - It will decrease the sum of any future subarray.
    - Therefore, we discard it and start a new subarray.

We maintain two variables:

1. currSum:
   - Represents the sum of the current subarray.

2. maxSum:
   - Represents the maximum subarray sum found so far.


Example:
--------
nums = [-2,1,-3,4,-1,2,1,-5,4]


Start:
maxSum = -2
currSum = 0


Process:

-2:
currSum = -2
maxSum = -2

Since currSum is negative, reset it.

1:
currSum = 1
maxSum = 1

-3:
currSum = -2

Reset because it is negative.

4:
currSum = 4
maxSum = 4

-1:
currSum = 3

2:
currSum = 5

1:
currSum = 6
maxSum = 6


Answer:
6


===============================================================================
Complexity Analysis
===============================================================================

Time Complexity:
----------------
O(n)

We iterate through the array only once.


Space Complexity:
-----------------
O(1)

Only two variables are used regardless of input size.


===============================================================================
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Maximum subarray sum found so far.
        #
        # Initialize with the first element because
        # the array may contain only negative numbers.
        maxSum = nums[0]

        # Current subarray sum.
        currSum = 0

        # Traverse through every element in the array.
        for i in nums:

            # If the current sum is negative,
            # discard it because it will reduce future sums.
            if currSum < 0:
                currSum = 0

            # Add current element to the current subarray.
            currSum += i

            # Update the maximum sum found so far.
            maxSum = max(maxSum, currSum)

        return maxSum


def main():
    """
    Driver function to test the solution.
    """

    solution = Solution()

    # Test Case 1
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    result = solution.maxSubArray(nums)

    print("=" * 60)
    print("Maximum Subarray - Kadane's Algorithm")
    print("=" * 60)

    print("Input Array :", nums)
    print("Maximum Sum :", result)

    print()

    # Test Case 2
    nums = [1]

    result = solution.maxSubArray(nums)

    print("Input Array :", nums)
    print("Maximum Sum :", result)

    print()

    # Test Case 3
    nums = [5, 4, -1, 7, 8]

    result = solution.maxSubArray(nums)

    print("Input Array :", nums)
    print("Maximum Sum :", result)

    print("=" * 60)


if __name__ == "__main__":
    main()