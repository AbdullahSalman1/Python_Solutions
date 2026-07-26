"""
LeetCode 11: Container With Most Water

Problem:
Given an integer array height where height[i] represents the height of a vertical line,
find two lines that together with the x-axis form a container that can store the
maximum amount of water.

The amount of water stored is calculated as:

    Area = Width * Minimum Height

Approach:
- Use the Two Pointer technique.
- Start with one pointer at the beginning and one at the end.
- Calculate the current area.
- Move the pointer with the smaller height because the shorter line limits the
  amount of water that can be stored.
- Continue until the two pointers meet.

Why Two Pointers?
A brute force approach checks every pair of lines, resulting in O(n²) time.
The two-pointer approach reduces this to O(n).

Time Complexity:
    O(n)

Space Complexity:
    O(1)
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Variable to store the maximum area found
        max_area = 0

        # Initialize two pointers:
        # left pointer starts from beginning
        # right pointer starts from end
        left, right = 0, len(height) - 1

        # Continue until the two pointers meet
        while left < right:

            # Calculate current container area:
            # Width = distance between pointers
            # Height = smaller of the two lines
            current_area = (right - left) * min(height[left], height[right])

            # Update maximum area
            max_area = max(max_area, current_area)

            # Move the pointer with the smaller height
            # because the smaller height limits the water level
            if height[left] < height[right]:
                left += 1

            elif height[right] < height[left]:
                right -= 1

            # If both heights are equal, move either pointer
            else:
                left += 1

        return max_area


# Driver Code
if __name__ == "__main__":

    # Example input
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]

    # Create object of Solution class
    solution = Solution()

    # Call the function
    result = solution.maxArea(heights)

    # Display output
    print("Input:", heights)
    print("Maximum Water Container Area:", result)