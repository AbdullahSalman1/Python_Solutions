"""
LeetCode Problem: 1249. Minimum Remove to Make Valid Parentheses

Problem:
Given a string s containing parentheses and lowercase English characters,
remove the minimum number of parentheses so that the resulting string is valid.

A valid parentheses string means:
- Every '(' has a matching ')'
- Every ')' has a matching '(' before it
- Parentheses are properly nested


Example:

Input:
s = "lee(t(c)o)de)"

Output:
"lee(t(c)o)de"


------------------------------------------------------------

Approach:
Stack + Mark Invalid Parentheses

Intuition:
While scanning the string, we need to find parentheses that do not have
matching pairs.

1. Store the indexes of opening parentheses '(' in a stack.
2. When we find a closing parenthesis ')':
      - If there is an opening parenthesis available, they form a valid pair.
        Remove the opening bracket from the stack.
      - Otherwise, this ')' is invalid, so mark it for removal.
3. After traversal, any '(' indexes remaining in the stack are unmatched,
   so remove them.
4. Join the remaining characters to get the final valid string.


Why Stack?
A stack follows the Last-In-First-Out (LIFO) property, which is perfect for
matching parentheses because the most recent '(' should match with the current ')'.

------------------------------------------------------------

Complexity Analysis:

Time Complexity:
O(n)

We traverse the string once. Each character is pushed and popped from the
stack at most once.

Space Complexity:
O(n)

The stack can contain all characters in the worst case if the string contains
only '(' characters.
------------------------------------------------------------
"""


class Solution:

    def minRemoveToMakeValid(self, s: str) -> str:

        # Convert string into a list because strings are immutable in Python.
        # Lists allow us to modify characters directly.
        chars = list(s)


        # Stack stores indexes of unmatched '(' characters.
        #
        # Example:
        # s = "a(b"
        #
        # When we see '(':
        # stack = [1]
        stack = []


        # Traverse the string and find invalid parentheses
        for i, ch in enumerate(chars):

            if ch == '(':

                # Store the index of opening parentheses.
                # We don't know yet if it has a matching ')'.
                stack.append(i)


            elif ch == ')':

                if stack:

                    # A matching '(' exists.
                    # Remove it from the stack because this pair is valid.
                    stack.pop()

                else:

                    # No '(' is available to match this ')'.
                    # Therefore this ')' is invalid and should be removed.
                    chars[i] = ""


        # Any remaining '(' in the stack are unmatched.
        # Remove them from the string.
        while stack:

            index = stack.pop()
            chars[index] = ""


        # Convert list of characters back into a string.
        # Empty strings are ignored during joining.
        return ''.join(chars)



def main():

    solution = Solution()


    # Test Case 1
    s1 = "lee(t(c)o)de)"

    print("Input :", s1)
    print("Output:", solution.minRemoveToMakeValid(s1))
    print()


    # Test Case 2
    s2 = "a)b(c)d"

    print("Input :", s2)
    print("Output:", solution.minRemoveToMakeValid(s2))
    print()


    # Test Case 3
    s3 = "))(("

    print("Input :", s3)
    print("Output:", solution.minRemoveToMakeValid(s3))
    print()


    # Additional Test Case
    s4 = "(a(b(c)d)"

    print("Input :", s4)
    print("Output:", solution.minRemoveToMakeValid(s4))



# Driver code
if __name__ == "__main__":
    main()