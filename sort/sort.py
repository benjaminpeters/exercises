############ Selection sort ############

def find_min(L, i):
    """Return the index of the smallest item in L[i:]."""

def selection_sort(L):
    """Sort the items in L in non-decreasing order."""

############ Insertion sort 1 ############

def insert(L, i):
    """Move L[i] to where it belongs in L[:i]"""

def insertion_sort_1(L):
    """Sort the items in L in non-decreasing order."""

############ Insertion sort 2 ############

def find_insertion_point(L, i):
    """Return the index where L[i] belongs in L[:i + 1]."""

def insertion_sort_2(L):
    """Sort the items in L in non-decreasing order."""

############ Bubblesort 1 ############

def bubblesort_1(L):
    """Sort the items in L in non-decreasing order."""

############ Bubblesort 2 ############

def bubblesort_2(L):
    """Sort the items in L in non-decreasing order."""

############ Mergesort 1 ############

def _merge_1(left, right):
    """Merge sorted lists left and right into a new list and return that new
    list."""

def _mergesort_1(L):
    """Return a new list that is a sorted version of list L."""

def mergesort_1(L):
    """Sort list L in non-decreasing order."""

############ Mergesort 2 ############

def _merge_2(L, i, mid, j):
    """Merge the two sorted halves L[i:mid + 1] and L[mid + 1:j + 1] and return
    them in a new list. Notice that L[mid] belongs in the left half and L[j]
    belongs in the right half -- the indices are inclusive."""

def _mergesort_2(L, i, j):
    """Sort the items in L[i] through L[j] in non-decreasing order."""

def mergesort_2(L):
    """Sort list L in non-decreasing order."""

############ Quicksort 1 ############

def _partition_1(L):
    """Rearrange L so that items < L[0] are at the beginning and items >= L[0]
    are at the end, and return the new index for L[0]."""

def _quicksort_1(L):
    """Sort L by partitioning it around the first item, then recursing."""

def quicksort_1(L):
    """Sort list L in non-decreasing order."""

############ Quicksort 2 ############

def _partition_2(L, i, j):
    """Rearrange L[i:j] so that items < L[i] are at the beginning and items
    >= L[i] are at the end, and return the new index for L[i]."""


def _quicksort_2(L, i, j):
    """Sort L[i:j] by partitioning it around the first item, then recursing."""

def quicksort_2(L):
    """Sort list L in non-decreasing order."""
