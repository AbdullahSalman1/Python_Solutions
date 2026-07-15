"""
Problem: 986. Interval List Intersections

Description:
You are given two lists of closed intervals, firstList and secondList.
Each list is sorted and contains disjoint intervals.

Return the intersection of these two interval lists.

Example:
Input:
firstList = [[0,2],[5,10],[13,23],[24,25]]
secondList = [[1,5],[8,12],[15,24],[25,26]]

Output:
[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]


Approach:
---------
Two Pointer Technique

Since both interval lists are sorted, we can process them simultaneously
using two pointers instead of comparing every interval with every interval.

For two intervals:
    [a, b] and [c, d]

The intersection is:

    start = max(a, c)
    end   = min(b, d)

If:
    start <= end

then an intersection exists, and we add [start, end] to the result.

After checking the intersection:
- Move the pointer of the interval that ends first.
- The interval that ends earlier cannot overlap with any future intervals
  because all intervals are sorted.


Time Complexity:
----------------
O(n + m)

n = number of intervals in firstList
m = number of intervals in secondList

Each pointer moves through its list only once.


Space Complexity:
-----------------
O(1)

Only pointers and variables are used.
The output list is not counted as extra space.
"""


class Solution:
    def intervalIntersection(self, firstList, secondList):

        # Stores all interval intersections
        output = []

        # Two pointers for both interval lists
        index1 = 0  # Pointer for firstList
        index2 = 0  # Pointer for secondList

        # Continue until we reach the end of either list
        while index1 < len(firstList) and index2 < len(secondList):

            # Calculate the possible intersection range
            # The intersection starts from the later start point
            start = max(firstList[index1][0], secondList[index2][0])

            # The intersection ends at the earlier end point
            end = min(firstList[index1][1], secondList[index2][1])

            # If start <= end, the intervals overlap
            # Example: [5,5] is also a valid closed interval
            if start <= end:
                output.append([start, end])

            # Move the pointer of the interval that finishes first
            #
            # The interval ending earlier cannot overlap with any future
            # intervals because the lists are sorted.
            if firstList[index1][1] < secondList[index2][1]:
                index1 += 1
            else:
                index2 += 1

        return output


# Driver code for testing
if __name__ == "__main__":

    solution = Solution()

    # Test Case 1
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]

    result = solution.intervalIntersection(firstList, secondList)

    print("Test Case 1:")
    print("Output:", result)
    print()


    # Test Case 2
    firstList = [[1,3],[5,9]]
    secondList = []

    result = solution.intervalIntersection(firstList, secondList)

    print("Test Case 2:")
    print("Output:", result)