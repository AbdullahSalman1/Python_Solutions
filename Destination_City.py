"""
Destination City Leetcode 1436 Problem

Problem:
You are given a list of paths where each path is represented as:
    [source_city, destination_city]

Each source city has a direct path to its destination city.

The paths form a single line with no loops, meaning there is exactly
one city that has no outgoing path. This city is called the
"destination city".

Example:
Input:
    [
        ["London", "New York"],
        ["New York", "Lima"],
        ["Lima", "Sao Paulo"]
    ]

Output:
    "Sao Paulo"

Explanation:
London -> New York -> Lima -> Sao Paulo

"Sao Paulo" has no outgoing path, so it is the destination city.

Approach:
1. Count outgoing paths for each city.
2. Every source city has at least one outgoing path.
3. Every destination city is added to the dictionary with an
   outgoing count of 0 if it does not already exist.
4. The city whose outgoing count remains 0 is the final destination.

Time Complexity: O(n)
Space Complexity: O(n)

LeetCode Problem:
https://leetcode.com/problems/destination-city/
"""


class Solution:
    def destCity(self, paths):
        """
        Returns the destination city.

        :param paths: List[List[str]]
        :return: str
        """

        # Dictionary to store the number of outgoing paths
        outgoing_count = {}

        # Process every path
        for source, destination in paths:

            # Source city has one more outgoing path
            outgoing_count[source] = outgoing_count.get(source, 0) + 1

            # Ensure destination city exists in the dictionary
            # without increasing its outgoing count
            outgoing_count[destination] = outgoing_count.get(destination, 0)

        # Find the city with zero outgoing paths
        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city


def main():
    """Driver code for testing."""

    solution = Solution()

    # Test Case 1
    paths1 = [
        ["London", "New York"],
        ["New York", "Lima"],
        ["Lima", "Sao Paulo"]
    ]
    print("Test Case 1 Output:", solution.destCity(paths1))

    # Test Case 2
    paths2 = [
        ["B", "C"],
        ["D", "B"],
        ["C", "A"]
    ]
    print("Test Case 2 Output:", solution.destCity(paths2))

    # Test Case 3
    paths3 = [
        ["A", "Z"]
    ]
    print("Test Case 3 Output:", solution.destCity(paths3))


if __name__ == "__main__":
    main()