"""
Chapter 1 - Algorithm Design: exercise solutions.

Run:  python solutions.py
"""


# ---------------- Exercise 1: smallest element ----------------
def find_min(arr):
    """Return the smallest element of arr. Time O(n), space O(1)."""
    if not arr:
        raise ValueError("array is empty")
    smallest = arr[0]
    for x in arr[1:]:
        if x < smallest:
            smallest = x
    return smallest


# ---------------- Exercise 2: count occurrences of x ----------------
def count_occurrences(arr, x):
    """Linear search that returns how many times x appears. Time O(n)."""
    count = 0
    for item in arr:
        if item == x:
            count += 1
    return count


# ---------------- Exercise 3: sum of even numbers ----------------
def sum_even(arr):
    """Return the sum of the even numbers in arr. Time O(n), space O(1)."""
    total = 0
    for x in arr:
        if x % 2 == 0:
            total += x
    return total


# ---------------- Exercise 4: tests (including boundary cases) ----------------
def test_find_min():
    assert find_min([5]) == 5              # boundary: one element
    assert find_min([3, 1, 2]) == 1        # normal case
    assert find_min([-5, -1, -9]) == -9    # negative numbers
    assert find_min([2, 2, 2]) == 2        # duplicates
    try:                                   # boundary: empty array
        find_min([])
    except ValueError:
        pass
    else:
        raise AssertionError("expected ValueError")


def test_count_occurrences():
    assert count_occurrences([], 4) == 0                 # boundary: empty
    assert count_occurrences([1, 2, 3], 9) == 0          # x not present
    assert count_occurrences([7, 7, 7], 7) == 3          # all equal to x
    assert count_occurrences([1, 2, 1, 3, 1], 1) == 3    # normal case


def test_sum_even():
    assert sum_even([]) == 0               # boundary: empty
    assert sum_even([1, 3, 5]) == 0        # no even numbers
    assert sum_even([2, 4, 6]) == 12       # all even
    assert sum_even([0, -2, 3, 4]) == 2    # zero and negatives


if __name__ == "__main__":
    test_find_min()
    test_count_occurrences()
    test_sum_even()
    print("All tests passed")
