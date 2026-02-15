"""
Merge Sort Implementation (Recursive)

This script implements the Merge Sort algorithm using a divide-and-conquer approach.

Algorithm Idea:
1. Divide the array into two halves.
2. Recursively sort both halves.
3. Merge the two sorted halves into one sorted array.

Time Complexity:
- Best Case: O(n log n)
- Average Case: O(n log n)
- Worst Case: O(n log n)

Reason:
- The array is divided into log n levels.
- At each level, merging takes O(n) time.
- Total = O(n log n)

Space Complexity:
- O(n) auxiliary space (for temporary subarrays)
"""

def merge_sort(arr):
    """
    Sorts the given list in ascending order using Merge Sort.

    Args:
        arr (list): List of comparable elements

    Returns:
        None (sorts the list in place)
    """
    if len(arr) > 1:
        # Step 1: Divide
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        # Recursively sort both halves
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Step 2: Merge
        i = j = k = 0

        # Compare elements from both halves
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Add remaining elements from left half (if any)
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Add remaining elements from right half (if any)
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


# Example usage
if __name__ == "__main__":
    sample_array = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", sample_array)

    merge_sort(sample_array)

    print("Sorted array:", sample_array)
