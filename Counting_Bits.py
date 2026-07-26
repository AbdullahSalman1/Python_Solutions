"""
LeetCode 338: Counting Bits

Problem:
Given an integer n, return an array ans of length n + 1 such that:
ans[i] is the number of 1's in the binary representation of i.

Example:
Input:
n = 5

Binary representations:
0 -> 0      (0 ones)
1 -> 1      (1 one)
2 -> 10     (1 one)
3 -> 11     (2 ones)
4 -> 100    (1 one)
5 -> 101    (2 ones)

Output:
[0, 1, 1, 2, 1, 2]


Approach:
Dynamic Programming with Offset

Observation:
Every number can be represented as:

    number = highest power of 2 + remaining value

Example:
5 = 4 + 1

Binary:
5 = 101
4 = 100
1 = 001

So:
bits(5) = 1 + bits(1)

We keep track of the latest power of 2 using the offset variable.
For every number i:
    dp[i] = 1 + dp[i - offset]

Time Complexity:
    O(n)

Space Complexity:
    O(n)
"""


from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:

        # Offset stores the most recent power of 2
        # Example:
        # 1, 2, 4, 8, ...
        offset = 1

        # dp[i] stores the number of 1 bits in the binary
        # representation of number i
        dp = [0] * (n + 1)

        # Calculate bit counts for numbers from 1 to n
        for i in range(1, n + 1):

            # When we reach the next power of 2,
            # update the offset value
            #
            # Example:
            # i = 2 -> offset becomes 2
            # i = 4 -> offset becomes 4
            if i == offset * 2:
                offset = i

            # Remove the highest set bit and reuse the previous result
            #
            # Example:
            # i = 5
            # offset = 4
            #
            # dp[5] = 1 + dp[5 - 4]
            #       = 1 + dp[1]
            #       = 1 + 1
            #       = 2
            dp[i] = 1 + dp[i - offset]

        # Return bit counts from 0 to n
        return dp


# Driver Code
if __name__ == "__main__":

    # Test input
    n = 5

    # Create Solution object
    solution = Solution()

    # Call function
    result = solution.countBits(n)

    # Display output
    print("Input:", n)
    print("Number of set bits from 0 to n:", result)