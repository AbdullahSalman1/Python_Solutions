"""
Majority Element Finder (Using Hash Map)

This script finds the majority element in an array, i.e., the element that appears
more than n/2 times. If no such element exists, it returns None.

Algorithm Idea:
- Use a hash map (dictionary) to count occurrences of each element.
- Check if any element occurs more than len(array)//2 times.

Time Complexity: O(n)  --> single pass to count, single pass to check
Space Complexity: O(n) --> hash map stores counts of all distinct elements
"""

def find_majority_element(arr):
    """
    Finds the majority element in the array using a hash map.

    Args:
        arr (list): List of elements (integers)

    Returns:
        int or None: Majority element if exists, else None
    """
    count_map = {}

    # Count occurrences of each element
    for number in arr:
        count_map[number] = count_map.get(number, 0) + 1

    # Check for majority element
    for number, count in count_map.items():
        if count > len(arr) // 2:
            return number

    return None

# Example usage
if __name__ == "__main__":
    sample_array = [3, 3, 4, 2, 4, 4, 2, 4, 4]
    print("Array:", sample_array)
    majority = find_majority_element(sample_array)
    if majority is not None:
        print("Majority element:", majority)
    else:
        print("No majority element found.")
