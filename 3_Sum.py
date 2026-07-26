"""
LeetCode 15: 3Sum

Problem:
Given an integer array nums, return all the unique triplets 
[nums[i], nums[j], nums[k]] such that:

    nums[i] + nums[j] + nums[k] == 0

Approach:
- Sort the array first.
- Fix one number and use two pointers to find the other two numbers.
- Skip duplicates to avoid repeated triplets.

Time Complexity:
    O(n^2)

Space Complexity:
    O(1) extra space (excluding output list)
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        # Stores all valid triplets
        res = []

        # Sorting allows us to use two pointers
        # and easily skip duplicate values
        nums.sort()

        # Iterate through each number as the first element
        for i, a in enumerate(nums):

            # Skip duplicate values for the first element
            # to avoid duplicate triplets
            if i > 0 and a == nums[i - 1]:
                continue

            # Two pointer initialization
            left = i + 1
            right = len(nums) - 1

            # Search for pairs that complete the triplet
            while left < right:

                total = a + nums[left] + nums[right]

                # Sum is too large, decrease right pointer
                if total > 0:
                    right -= 1

                # Sum is too small, increase left pointer
                elif total < 0:
                    left += 1

                # Found a valid triplet
                else:
                    res.append([a, nums[left], nums[right]])

                    # Move both pointers to continue searching
                    left += 1
                    right -= 1

                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate values for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return res


# Driver code to test the solution
if __name__ == "__main__":

    solution = Solution()

    nums = [-1, 0, 1, 2, -1, -4]

    result = solution.threeSum(nums)

    print("Input:", nums)
    print("Triplets with sum 0:", result)