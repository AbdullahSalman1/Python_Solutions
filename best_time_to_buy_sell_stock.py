"""
===============================================================================
              Best Time to Buy and Sell Stock (LeetCode 121)
                        Two Pointer Approach
===============================================================================

Problem:
--------
You are given an array where prices[i] represents the stock price on day i.

You need to choose:
1. One day to buy a stock.
2. A different day in the future to sell that stock.

Return the maximum profit possible.

If no profit can be made, return 0.


Example:
--------
Input:
prices = [7,1,5,3,6,4]

Output:
5

Explanation:
Buy on day 2 at price 1.
Sell on day 5 at price 6.

Profit = 6 - 1 = 5


===============================================================================
Approach: Two Pointers
===============================================================================

Idea:
-----
We maintain two pointers:

left  -> buying day
right -> selling day


The left pointer should always represent the cheapest buying price seen so far.

For every selling day:

1. If prices[right] > prices[left]:
      - We can make a profit.
      - Calculate the profit.
      - Update the maximum profit.

2. Otherwise:
      - The current price is lower than our buying price.
      - This is a better day to buy.
      - Move the left pointer to the current day.


Example:
--------
prices = [7,1,5,3,6,4]


Start:
left = 7
right = 1

1 < 7:
Move left to 1.


Now:
Buy = 1
Sell = 5

Profit = 5 - 1 = 4


Later:
Buy = 1
Sell = 6

Profit = 6 - 1 = 5


Maximum profit = 5


===============================================================================
Complexity Analysis
===============================================================================

Time Complexity:
----------------
O(n)

We traverse the array only once using the right pointer.


Space Complexity:
-----------------
O(1)

We only use a few variables, regardless of input size.

===============================================================================
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Two pointers:
        #
        # left  -> buying day
        # right -> selling day
        left, right = 0, 1

        # Stores the maximum profit found so far
        maxProfit = 0

        # Move right pointer through the array
        while right < len(prices):

            # If selling price is greater than buying price,
            # calculate possible profit
            if prices[right] > prices[left]:

                profit = prices[right] - prices[left]

                # Keep track of the best profit
                maxProfit = max(maxProfit, profit)

            else:
                # Found a cheaper buying price.
                #
                # Example:
                # Buy at 7
                # Current price is 3
                #
                # Buying at 3 is better because it can
                # create a larger profit in the future.
                left = right

            # Move to the next selling day
            right += 1

        return maxProfit


def main():
    """
    Main function to test the solution.
    """

    solution = Solution()

    # Test Case 1
    prices = [7, 1, 5, 3, 6, 4]

    result = solution.maxProfit(prices)

    print("=" * 50)
    print("Best Time to Buy and Sell Stock")
    print("=" * 50)

    print("Stock Prices :", prices)
    print("Maximum Profit:", result)

    print()

    # Test Case 2
    prices = [7, 6, 4, 3, 1]

    result = solution.maxProfit(prices)

    print("Stock Prices :", prices)
    print("Maximum Profit:", result)

    print("=" * 50)


if __name__ == "__main__":
    main()