"""
===============================================================================
                        Two Sum (Hash Map Approach)
===============================================================================

Problem:
--------
Given an array of integers 'nums' and an integer 'target', return the indices
of the two numbers such that they add up to the target.

Assumptions:
------------
- Exactly one valid solution exists.
- The same element cannot be used twice.

Example:
--------
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Explanation:
nums[0] + nums[1] = 2 + 7 = 9

===============================================================================
Approach
===============================================================================

Instead of checking every possible pair (which takes O(n²) time), we use a
Hash Map (Python Dictionary).

The dictionary stores:
    Number -> Index

Example:
---------
{
    2: 0,
    7: 1,
    11: 2
}

For every number in the array:

1. Calculate the number required to reach the target.

       required = target - current_number

2. Check if this required number already exists in the dictionary.

       If yes:
           We have found the answer.

       If no:
           Store the current number and its index.

This allows us to solve the problem in a single traversal.

===============================================================================
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two indices whose corresponding values add up to the target.

        Parameters
        ----------
        nums : List[int]
            Input array of integers.

        target : int
            Desired sum.

        Returns
        -------
        List[int]
            Indices of the two numbers whose sum equals the target.
        """

        # Dictionary that stores:
        #
        # Key   -> Number
        # Value -> Index
        #
        # Example:
        # {
        #     2 : 0,
        #     7 : 1,
        #     11 : 2
        # }
        hash_map = {}

        # enumerate() returns both the index and the value.
        #
        # Example:
        #
        # nums = [2, 7, 11]
        #
        # Iteration 1:
        # index = 0
        # val = 2
        #
        # Iteration 2:
        # index = 1
        # val = 7
        #
        # Iteration 3:
        # index = 2
        # val = 11
        for index, val in enumerate(nums):

            # Calculate the number needed to reach the target.
            #
            # Example:
            #
            # target = 9
            # val = 2
            #
            # required = 9 - 2 = 7
            diff = target - val

            # If the required number already exists in the dictionary,
            # we have found the pair.
            #
            # Example:
            #
            # hash_map = {2: 0}
            # current value = 7
            #
            # diff = 9 - 7 = 2
            #
            # Since 2 exists inside hash_map,
            # return [0, 1]
            if diff in hash_map:
                return [hash_map[diff], index]

            # Otherwise, store the current number and its index.
            #
            # Example:
            #
            # hash_map[2] = 0
            hash_map[val] = index

        # This line is never reached because the problem
        # guarantees exactly one valid solution.
        return []


def main():
    """
    Driver function to test the solution.
    """

    solution = Solution()

    # Example Test Case
    nums = [2, 7, 11, 15]
    target = 9

    print("=" * 50)
    print("Two Sum")
    print("=" * 50)

    print(f"Input Array : {nums}")
    print(f"Target      : {target}")

    answer = solution.twoSum(nums, target)

    print(f"Indices     : {answer}")

    # Display the actual numbers found
    if answer:
        i, j = answer
        print(f"Numbers     : {nums[i]} + {nums[j]} = {target}")

    print("=" * 50)


if __name__ == "__main__":
    main()