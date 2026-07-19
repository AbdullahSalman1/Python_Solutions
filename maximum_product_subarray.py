"""
LeetCode 152. Maximum Product Subarray
Difficulty: Medium

Problem:
Given an integer array nums, find the subarray with the largest product,
and return the product.

Example:

Input:
nums = [2,3,-2,4]

Output:
6

Explanation:
The subarray [2,3] has the maximum product:
2 * 3 = 6


Approach:
We use a modified version of Kadane's Algorithm.

For maximum sum subarray, we only track the maximum value.
For maximum product subarray, we track both:

1. currMax:
   Maximum product ending at the current index.

2. currMin:
   Minimum product ending at the current index.

Why currMin?
A negative product can become the maximum product when multiplied
by another negative number.

Example:
currMin = -6
current number = -4

-6 * -4 = 24  (new maximum product)


Time Complexity:
O(n)

Space Complexity:
O(1)
"""


class Solution:
    def maxProduct(self, nums):
        """
        Finds the maximum product of a contiguous subarray.
        """

        # Initialize result with the largest element.
        # The answer can be a single element.
        result = max(nums)

        # Track maximum and minimum product ending at current index.
        # Start with 1 because it is the multiplicative identity.
        currMax = 1
        currMin = 1

        for n in nums:

            # Store previous currMax because we need it
            # when calculating currMin.
            temp = currMax * n

            # The current maximum product can come from:
            # 1. Starting a new subarray from n
            # 2. Extending previous maximum product
            # 3. Extending previous minimum product
            #
            # The third case handles negative numbers.
            currMax = max(
                n,
                currMax * n,
                currMin * n
            )

            # The current minimum product is needed because
            # it may become the maximum later after multiplying
            # by another negative number.
            currMin = min(
                n,
                temp,
                currMin * n
            )

            # Update global maximum answer.
            result = max(result, currMax)

        return result


def main():
    """
    Driver code to test the solution.
    """

    solution = Solution()

    # Test Case 1
    nums = [2, 3, -2, 4]

    print("Input:")
    print(nums)

    print("Maximum Product:")
    print(solution.maxProduct(nums))


    # Test Case 2
    nums = [-2, 0, -1]

    print("\nInput:")
    print(nums)

    print("Maximum Product:")
    print(solution.maxProduct(nums))


    # Test Case 3
    nums = [-2, 3, -4]

    print("\nInput:")
    print(nums)

    print("Maximum Product:")
    print(solution.maxProduct(nums))


if __name__ == "__main__":
    main()