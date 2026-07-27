# LeetCode 70: Climbing Stairs
#
# Problem:
# You are climbing a staircase with n steps.
# Each time, you can climb either 1 step or 2 steps.
# Return the number of distinct ways to reach the top.
#
# Example:
# Input: n = 5
# Output: 8
#
# Explanation:
# The possible ways are:
# 1+1+1+1+1
# 1+1+1+2
# 1+1+2+1
# 1+2+1+1
# 2+1+1+1
# 1+2+2
# 2+1+2
# 2+2+1


class Solution:
    def climbStairs(self, n: int) -> int:

        # The problem follows the Fibonacci pattern:
        #
        # ways(n) = ways(n-1) + ways(n-2)
        #
        # To reach the nth stair:
        # - We can come from the (n-1)th stair by taking 1 step.
        # - We can come from the (n-2)th stair by taking 2 steps.
        #
        # Instead of storing all previous results in an array,
        # we only keep track of the last two values to save space.

        # one -> number of ways to reach the current step
        # two -> number of ways to reach the previous step
        #
        # Initially:
        # ways(1) = 1
        # ways(0) = 1
        one, two = 1, 1

        # Calculate the Fibonacci sequence iteratively.
        for _ in range(n - 1):

            # Store the current value before updating it
            temp = one

            # Current number of ways is the sum of previous two states
            one = one + two

            # Move the previous value forward
            two = temp

        # After the loop, one contains ways(n)
        return one


# Time Complexity:
# O(n)
# We iterate through the staircase once.

# Space Complexity:
# O(1)
# Only two variables are used to store previous results.