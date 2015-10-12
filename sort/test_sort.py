from sort import *
import random

def is_sorted(L):
    """Return True iff L is in non-decreasing order."""
    for i in range(1, len(L)):
        if L[i - 1] > L[i]:
            return False
    return True

def generate_data(n, sorted=False, reversed=False):
    """Return a list of n ints. If sorted, the list should be nearly sorted:
    only a few elements are out of order. If sorted and reversed, the list
    should be nearly sorted in reverse. The list should otherwise be shuffled
    (in random order)."""
    L = [2 * i for i in range(n)]
    if sorted:
        i = random.randrange(5, 11)
        while i < n // 2:
            L[i], L[-i] = L[-i], L[i]
            i += random.randrange(5, 11)
        if reversed:
            L.reverse()
    else:
        random.shuffle(L)
    return L

def sort_data(which_sort, data):
    """Run each algorithm on the generated list, then print whether or not it
    was sorted."""
    sorter_name = which_sort.__name__  # the function's name as a string
    
    # Verify that the sorting algorithm works correctly!
    new_L = L[:]
    which_sort(new_L)
    assert is_sorted(new_L) and new_L == sorted(L), sorter_name + " did not sort"    
    
    print("{} sorted\n".format(sorter_name))
    
if __name__ == "__main__":
    for algo in [selection_sort, insertion_sort_1, bubblesort_1,
                 mergesort_1, quicksort_1]:
        L = generate_data(100)
        sort_data(algo, L)