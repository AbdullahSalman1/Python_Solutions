"""
===========================================================
Longest Increasing Subsequence (LeetCode 300)
===========================================================

Problem:
Given an integer array `nums`, return the length of the
Longest Increasing Subsequence (LIS).

A subsequence is a sequence that can be derived from an array
by deleting some or no elements without changing the order of
the remaining elements.

Example:
Input:
nums = [10, 9, 2, 5, 3, 7, 101, 18]

Output:
4

Explanation:
The longest increasing subsequence is [2, 3, 7, 101],
so the answer is 4.

-----------------------------------------------------------
Approach: Bottom-Up Dynamic Programming (Tabulation)
-----------------------------------------------------------

Idea:
For every index i, compute the length of the longest increasing
subsequence that STARTS from index i.

We process the array from right to left because the answer for
the current element depends on elements that come after it.

DP Definition:
dp[i] = Length of the Longest Increasing Subsequence
        starting at index i.

Initialization:
Every element can always form an increasing subsequence of
length 1 (itself).

Transition:
For every index i:
    Look at every index j > i.

    If nums[i] < nums[j]:
        We can extend the subsequence.

        dp[i] = max(dp[i], 1 + dp[j])

Finally, the answer is simply the maximum value inside dp.

-----------------------------------------------------------
Time Complexity:
O(n²)

Two nested loops are used.

-----------------------------------------------------------
Space Complexity:
O(n)

The DP array stores one value for each element.

-----------------------------------------------------------
"""


from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Returns the length of the Longest Increasing Subsequence.

        Parameters
        ----------
        nums : List[int]
            Input array.

        Returns
        -------
        int
            Length of the longest increasing subsequence.
        """

        # Edge case
        if not nums:
            return 0

        # dp[i] stores the LIS length starting from index i.
        dp = [1] * len(nums)

        # Traverse from right to left because each state depends
        # on values located after the current index.
        for i in range(len(nums) - 1, -1, -1):

            # Compare nums[i] with every element after it.
            for j in range(i + 1, len(nums)):

                # If nums[j] is larger, it can extend
                # the increasing subsequence.
                if nums[i] < nums[j]:

                    # Keep the longest subsequence possible.
                    dp[i] = max(dp[i], 1 + dp[j])

        # The LIS can start from any index.
        return max(dp)


# ----------------------------------------------------------
# Example Usage
# ----------------------------------------------------------
if __name__ == "__main__":

    nums = [10, 9, 2, 5, 3, 7, 101, 18]

    solution = Solution()

    answer = solution.lengthOfLIS(nums)

    print("Input :", nums)
    print("Length of Longest Increasing Subsequence:", answer)