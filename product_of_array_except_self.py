"""
LeetCode 238. Product of Array Except Self
Difficulty: Medium

Problem:
Given an integer array 'nums', return an array 'answer' such that
answer[i] is equal to the product of all the elements of nums except nums[i].

Constraints:
- Do not use division.
- The algorithm must run in O(n) time.

Example:
Input:
nums = [1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Explanation:
For each index, multiply every element except the current one.

Index 0:
2 × 3 × 4 = 24

Index 1:
1 × 3 × 4 = 12

Index 2:
1 × 2 × 4 = 8

Index 3:
1 × 2 × 3 = 6
"""


class Solution:
    def productExceptSelf(self, nums):
        """
        Returns an array where each element is the product of all
        elements except itself.

        Idea:
        -----
        Instead of using division, we calculate:

        1. Prefix Product
           Product of all elements to the LEFT of each index.

        2. Postfix Product
           Product of all elements to the RIGHT of each index.

        Multiplying these two values gives the answer for every index.
        """

        n = len(nums)

        # Result array.
        # Initially every value is 1 because
        # 1 is the multiplicative identity.
        result = [1] * n

        # ----------------------------------------------------
        # FIRST PASS (Left → Right)
        # Store prefix products.
        # ----------------------------------------------------
        #
        # Example:
        # nums = [1,2,3,4]
        #
        # prefix starts as 1
        #
        # i=0 -> result[0]=1
        # prefix = 1
        #
        # i=1 -> result[1]=1
        # prefix = 2
        #
        # i=2 -> result[2]=2
        # prefix = 6
        #
        # i=3 -> result[3]=6
        #
        # result becomes:
        # [1,1,2,6]
        #

        prefix = 1

        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # ----------------------------------------------------
        # SECOND PASS (Right → Left)
        # Multiply postfix products.
        # ----------------------------------------------------
        #
        # Continuing the example:
        #
        # result = [1,1,2,6]
        #
        # postfix starts as 1
        #
        # i=3:
        # result[3] = 6 × 1 = 6
        # postfix = 4
        #
        # i=2:
        # result[2] = 2 × 4 = 8
        # postfix = 12
        #
        # i=1:
        # result[1] = 1 × 12 = 12
        # postfix = 24
        #
        # i=0:
        # result[0] = 1 × 24 = 24
        #
        # Final answer:
        # [24,12,8,6]
        #

        postfix = 1

        for i in range(n - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result


def main():
    """
    Driver code to demonstrate the algorithm.
    """

    solution = Solution()

    # Example 1
    nums = [1, 2, 3, 4]

    print("Input:")
    print(nums)

    answer = solution.productExceptSelf(nums)

    print("\nOutput:")
    print(answer)

    # Example 2
    nums = [-1, 1, 0, -3, 3]

    print("\nInput:")
    print(nums)

    answer = solution.productExceptSelf(nums)

    print("\nOutput:")
    print(answer)


if __name__ == "__main__":
    main()


"""
Time Complexity:
----------------
O(n)

We traverse the array twice:
1. Prefix pass
2. Postfix pass

Total = O(n)

Space Complexity:
-----------------
O(1) extra space

Only two variables (prefix and postfix) are used.
The output array is not counted as extra space according
to the problem statement.
"""