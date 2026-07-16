"""
LeetCode 528 - Random Pick with Weight

Problem:
Given an array of positive integers w, randomly pick an index where the
probability of selecting index i is:

        w[i] / sum(w)

Example:
w = [1, 3]

Index 0 probability = 1/4
Index 1 probability = 3/4


Approach:
---------
We use Prefix Sum + Binary Search.

Idea:
Imagine expanding the array according to weights.

Example:
w = [2,5,3]

Expanded array would be:

[0,0,1,1,1,1,1,2,2,2]

Now every position has equal probability.

Instead of creating this large array, we store only the boundaries
using prefix sums.

Prefix sum:

[2,7,10]

Meaning:

1-2     -> index 0
3-7     -> index 1
8-10    -> index 2

Then:
1. Generate a random number between 1 and total weight.
2. Use binary search to find the first prefix sum >= target.
3. Return that index.


Time Complexity:
---------------
__init__():
    O(n) - Building prefix sum array.

pickIndex():
    O(log n) - Binary search on prefix sum array.


Space Complexity:
-----------------
O(n) - Storing prefix sum array.
"""


import random
from typing import List


class Solution:

    def __init__(self, w: List[int]):

        # Stores cumulative weights
        # Example:
        # w = [2,5,3]
        #
        # prefixSum becomes:
        # [2,7,10]
        #
        # Each value represents the end of a range.

        self.prefixSum = []

        self.prefixSum.append(w[0])

        for i in range(1, len(w)):
            self.prefixSum.append(self.prefixSum[-1] + w[i])


    def pickIndex(self) -> int:

        # Generate a random ticket number.
        #
        # Total weight is the last value in prefixSum.
        #
        # Example:
        # prefixSum = [2,7,10]
        #
        # Random number can be from 1 to 10.

        target = random.randint(1, self.prefixSum[-1])


        # Binary search to find the first prefix sum
        # that is greater than or equal to target.
        #
        # Example:
        #
        # prefixSum = [2,7,10]
        # target = 6
        #
        # First value >= 6 is 7
        # Index = 1
        #
        # Therefore return 1.

        left = 0
        right = len(self.prefixSum) - 1


        while left < right:

            mid = (left + right) // 2


            if self.prefixSum[mid] < target:

                # Current range is too small.
                # Move to the right side.

                left = mid + 1

            else:

                # mid can be the answer,
                # but there might be a smaller valid index.
                # Continue searching on the left side.

                right = mid


        return left



# -----------------------------
# Testing the solution locally
# -----------------------------

if __name__ == "__main__":

    weights = [1, 3]

    solution = Solution(weights)


    print("Weights:", weights)

    print("Random selections:")

    for _ in range(10):
        print(solution.pickIndex())