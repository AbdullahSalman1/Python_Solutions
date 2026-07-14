

"""
LeetCode Problem: 767. Reorganize String

Problem:
Given a string s, rearrange the characters of s so that no two adjacent
characters are the same.

Example:
Input:  s = "aab"
Output: "aba"

Input:  s = "aaab"
Output: ""

------------------------------------------------------------

Approach:
Greedy + Max Heap (Priority Queue)

Intuition:
The character with the highest frequency has the biggest chance of creating
adjacent duplicates. Therefore, at every step, we always pick the character
with the highest remaining frequency.

However, after using a character, we cannot use it again immediately.
So we temporarily store the previous character and put it back into the heap
only after selecting another character.

Algorithm:
1. Count the frequency of every character.
2. Store characters in a max heap based on frequency.
   - Python has a min heap, so we store frequencies as negative values.
3. If the most frequent character appears more than (n+1)//2 times,
   rearrangement is impossible.
4. Use the heap:
      - Remove the character with maximum frequency.
      - Add it to the answer.
      - Put the previous character back into the heap if it still has
        remaining frequency.
5. Return the generated string.

------------------------------------------------------------

Complexity Analysis:

Let:
n = length of the string
k = number of unique characters

Time Complexity:
O(n log k)

Reason:
Each character is pushed and popped from the heap.
Heap operations take O(log k).

Space Complexity:
O(k)

Reason:
We store the frequency map and heap containing unique characters.

------------------------------------------------------------
"""


from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:

        # Step 1:
        # Count frequency of each character
        #
        # Example:
        # s = "aab"
        #
        # frequency:
        # {
        #   'a': 2,
        #   'b': 1
        # }
        freq = Counter(s)


        # Step 2:
        # Create a max heap based on character frequency
        #
        # Python provides only a MIN heap.
        # Therefore, we store frequency as negative.
        #
        # Example:
        # a appears 3 times
        # stored as:
        # (-3, 'a')
        #
        # The smallest negative value represents
        # the largest frequency.
        heap = [(-count, char) for char, count in freq.items()]

        heapq.heapify(heap)


        # Step 3:
        # Check if rearrangement is possible
        #
        # If the most frequent character appears more than
        # half of the string, we cannot place it without
        # creating adjacent duplicates.
        #
        # Example:
        # "aaab"
        #
        # a appears 3 times
        # maximum allowed = (4+1)//2 = 2
        #
        # Since 3 > 2, answer is impossible.
        if -heap[0][0] > (len(s) + 1) // 2:
            return ""


        result = ""

        # Stores the previously used character.
        #
        # We keep this character outside the heap temporarily
        # because the next character cannot be the same.
        #
        # Format:
        # (remaining_frequency, character)
        previous = (0, "")


        # Step 4:
        # Build the answer using greedy approach
        while heap:

            # Select character with highest frequency
            count, char = heapq.heappop(heap)


            # Add selected character to answer
            result += char


            # Now the previous character can safely return
            # to the heap because we already placed a different
            # character.
            if previous[0] < 0:
                heapq.heappush(heap, previous)


            # Decrease the frequency of current character
            #
            # Since counts are negative:
            #
            # -5 -> -4
            #
            # We increase the count by 1.
            previous = (count + 1, char)


        return result



def main():

    solution = Solution()


    # Test Case 1
    s1 = "aab"

    answer1 = solution.reorganizeString(s1)

    print("Input:", s1)
    print("Output:", answer1)
    print()


    # Test Case 2
    s2 = "aaab"

    answer2 = solution.reorganizeString(s2)

    print("Input:", s2)
    print("Output:", answer2)
    print()


    # Additional Test Cases

    s3 = "vvvlo"

    answer3 = solution.reorganizeString(s3)

    print("Input:", s3)
    print("Output:", answer3)



if __name__ == "__main__":
    main()