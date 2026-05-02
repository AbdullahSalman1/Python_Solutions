
# Priority Queue implementation using Min Heap

#
# This file implements a priority queue using a min-heap data structure.
#
# Time Complexities:
# - insert: O(log n)
# - extract_min: O(log n)
# - peek_min: O(1)
# - heapify: O(n)
# - meld: O(n)

# MinHeap class definition



class MinHeap:
    """
    MinHeap implements a priority queue using a binary min-heap.
    """
    def __init__(self):
        # Initialize an empty heap
        self.heap = []

    def __len__(self):
        # Return the number of elements in the heap
        return len(self.heap)

    def __repr__(self):
        # String representation of the heap
        return str(self.heap)

    def insert(self, key):
        """
        Insert a new key into the heap.
        Time Complexity: O(log n)
        """
        self.heap.append(key)
        self._sift_up(len(self.heap) - 1)

    def peek_min(self):
        """
        Return the minimum element without removing it.
        Time Complexity: O(1)
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def extract_min(self):
        """
        Remove and return the minimum element from the heap.
        Time Complexity: O(log n)
        """
        if not self.heap:
            raise IndexError("Heap is empty")
        min_element = self.heap[0]
        last_element = self.heap.pop()
        if self.heap:
            self.heap[0] = last_element
            self._sift_down(0)
        return min_element

    def heapify(self, elements):
        """
        Build a heap from an iterable of elements.
        Time Complexity: O(n)
        """
        self.heap = list(elements)
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self._sift_down(i)

    def meld(self, other_heap):
        """
        Meld (combine) another heap into this heap.
        Time Complexity: O(n)
        """
        combined_heap = self.heap + other_heap.heap
        self.heapify(combined_heap)

    def _parent(self, index):
        # Return the parent index of a given node
        return (index - 1) // 2 if index > 0 else None

    def _left(self, index):
        # Return the left child index if exists
        left = 2 * index + 1
        return left if left < len(self.heap) else None

    def _right(self, index):
        # Return the right child index if exists
        right = 2 * index + 2
        return right if right < len(self.heap) else None

    def _sift_up(self, index):
        # Move the element at index up to maintain heap property
        parent_index = self._parent(index)
        if parent_index is not None and self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._sift_up(parent_index)

    def _sift_down(self, index):
        # Move the element at index down to maintain heap property
        smallest = index
        left_index = self._left(index)
        right_index = self._right(index)
        if left_index is not None and self.heap[left_index] < self.heap[smallest]:
            smallest = left_index
        if right_index is not None and self.heap[right_index] < self.heap[smallest]:
            smallest = right_index
        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._sift_down(smallest)


# -------------------
# Main and Test Cases
# -------------------

def main():
    print("Testing MinHeap (Priority Queue) implementation:\n")

    # Test 1: Insert and extract_min
    heap = MinHeap()
    elements = [5, 3, 8, 1, 2]
    print(f"Inserting elements: {elements}")
    for el in elements:
        heap.insert(el)
        print(f"Heap after inserting {el}: {heap}")
    print(f"Minimum element (peek): {heap.peek_min()}")
    print(f"Extracting min: {heap.extract_min()}")
    print(f"Heap after extract_min: {heap}\n")

    # Test 2: Heapify
    arr = [10, 4, 7, 9, 1]
    heap2 = MinHeap()
    heap2.heapify(arr)
    print(f"Heapified array {arr}: {heap2}")
    print(f"Extracting all elements:")
    while len(heap2) > 0:
        print(heap2.extract_min(), end=' ')
    print("\n")

    # Test 3: Meld
    heap3 = MinHeap()
    heap4 = MinHeap()
    for el in [6, 2, 9]:
        heap3.insert(el)
    for el in [5, 1, 8]:
        heap4.insert(el)
    print(f"Heap3: {heap3}")
    print(f"Heap4: {heap4}")
    heap3.meld(heap4)
    print(f"Melded Heap: {heap3}\n")

    # Test 4: Edge cases
    empty_heap = MinHeap()
    try:
        empty_heap.extract_min()
    except IndexError as e:
        print(f"Correctly caught error on extract_min from empty heap: {e}")
    try:
        empty_heap.peek_min()
    except IndexError as e:
        print(f"Correctly caught error on peek_min from empty heap: {e}")


if __name__ == "__main__":
    main()

        

        
        




