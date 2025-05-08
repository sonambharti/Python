"""
Sort an array using heap sort. 
"""

import heapq

"""
The brute force idea is:
1.  Push all elements into a min-heap (i.e., priority queue).
2.  Pop elements one by one and store them in the array — this gives us sorted elements.

⏱️ Time & Space Complexity (Brute Force)
Time: O(n log n) (each insertion/removal in heap is log n)
Space: O(n) for extra heap space
"""
def heap_sort_brute_force(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    
    for i in range(len(arr)):
        arr[i] = heapq.heappop(heap)


"""
🔹 Optimal Approach — In-Place Heap Sort

Use max-heap logic and do the following steps:

Build a max-heap in the array.
Swap the first (largest) element with the last.
Reduce heap size by 1 and heapify the root.
Repeat until array is sorted.

⏱️ Time & Space Complexity (Optimal)
Time: O(n log n) (building heap = O(n), each heapify = O(log n), repeated n times)
Space: O(1) (in-place)
"""

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1   # left child
    right = 2 * i + 2  # right child

    # If left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Step 1: Build max heap (heapify all non-leaf nodes)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[0], arr[i] = arr[i], arr[0]
        # Heapify the reduced heap
        heapify(arr, i, 0)



if __name__ == "__main__":
  # Example
  arr = [5, 3, 8, 4, 1]
  heap_sort_brute_force(arr)
  print("Sorted array:", arr)

  arr1 = [5, 3, 8, 4, 1]
  heap_sort(arr1)
  print("Sorted array:", arr1)
