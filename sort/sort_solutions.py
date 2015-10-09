############ Selection sort ############

def find_min(L, i):
    """Return the index of the smallest item in L[i:]."""

    smallest = i
    for j in range(i + 1, len(L)):
        if L[j] < L[smallest]:
            smallest = j
    return smallest

# find_min using built-in min, tuple comparisons, and enumerate
# should be faster...
#def find_min(L, i):
    #"""Return index of smallest item in L[i:]."""
    #return min([(k, j) for j, k in enumerate(L[i:])])[1] + i

def selection_sort(L):
    """Sort the items in L in non-decreasing order."""

    i = 0
    while i != len(L) - 1:

        # Find the smallest remaining item and move it to index i.
        smallest = find_min(L, i)
        L[smallest], L[i] = L[i], L[smallest]
        i += 1


############ Insertion sort 1 ############

def insert(L, i):
    """Move L[i] to where it belongs in L[:i]"""

    v = L[i]
    while i > 0 and L[i - 1] > v:
        L[i] = L[i - 1]
        i -= 1
    L[i] = v

def insertion_sort_1(L):
    """Sort the items in L in non-decreasing order."""

    i = 1

    # Insert each item i where it belongs in L[0:i + 1]
    while i != len(L):
        insert(L, i)
        i += 1

############ Insertion sort 2 ############

def find_insertion_point(L, i):
    """Return the index where L[i] belongs in L[:i + 1]."""

    v = L[i]
    while i > 0 and L[i - 1] > v:
        i -= 1

    return i

def insertion_sort_2(L):
    """Sort the items in L in non-decreasing order."""

    i = 1

    # Insert each item i where it belongs in L[0:i + 1]
    while i != len(L):
        the_spot = find_insertion_point(L, i)
        v = L[i]
        del L[i]
        L.insert(the_spot, v)
        i += 1


############ Bubblesort 1 ############

def bubblesort_1(L):
    """Sort the items in L in non-decreasing order."""

    j = len(L) - 1
    while j != 0:

        # Swap every item that is out of order.
        for i in range(j):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
        j -= 1

############ Bubblesort 2 ############

def bubblesort_2(L):
    """Sort the items in L in non-decreasing order."""

    j = len(L) - 1
    swapped = True

    # Stop when no elements are swapped.
    while swapped and j != 0:
        swapped = False

        # Swap every item that is out of order.
        for i in range(j):
            if L[i] > L[i + 1]:
                swapped = True
                L[i], L[i + 1] = L[i + 1], L[i]
        j -= 1


############ Mergesort 1 ############

def _merge_1(left, right):
    """Merge sorted lists left and right into a new list and return that new
    list."""

    result = []

    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]
    return result

def _mergesort_1(L):
    """Return a new list that is a sorted version of list L."""

    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = _mergesort_1(L[:middle])
        right = _mergesort_1(L[middle:])
    return _merge_1(left, right)

def mergesort_1(L):
    """Sort list L in non-decreasing order."""

    L[:] = _mergesort_1(L)

############ Mergesort 2 ############

def _merge_2(L, i, mid, j):
    """Merge the two sorted halves L[i:mid + 1] and L[mid + 1:j + 1] and return
    them in a new list. Notice that L[mid] belongs in the left half and L[j]
    belongs in the right half -- the indices are inclusive."""

    result = []
    left = i
    right = mid + 1

    # Done when left > mid or when right > j; i.e., when we've finished one of
    # the halves.
    while left <= mid and right <= j:
        if L[left] < L[right]:
            result.append(L[left])
            left += 1
        else:
            result.append(L[right])
            right += 1

    # Items left: L[left:mid + 1]
    #             L[right:j + 1]
    return result + L[left:mid + 1] + L[right:j + 1]

def _mergesort_2(L, i, j):
    """Sort the items in L[i] through L[j] in non-decreasing order."""

    if i < j:
        mid = (i + j) // 2
        _mergesort_2(L, i, mid)
        _mergesort_2(L, mid + 1, j)
        L[i:j + 1] = _merge_2(L, i, mid, j)

def mergesort_2(L):
    """Sort list L in non-decreasing order."""

    _mergesort_2(L, 0, len(L) - 1)


############ Quicksort 1 ############

def _partition_1(L):
    """Rearrange L so that items < L[0] are at the beginning and items >= L[0]
    are at the end, and return the new index for L[0]."""

    v = L[0]
    i = 1
    j = len(L) - 1
    while i <= j:
        if L[i] < v:
            i += 1
        else:
            L[i], L[j] = L[j], L[i]
            j -= 1

    L[0], L[j] = L[j], L[0]
    return j

def _quicksort_1(L):
    """Sort L by partitioning it around the first item, then recursing."""

    if len(L) <= 1:
        return L
    else:
        pivot = _partition_1(L)
        left = L[:pivot]
        right = L[pivot + 1:]
        return _quicksort_1(left) + [L[pivot]] + _quicksort_1(right)

def quicksort_1(L):
    """Sort list L in non-decreasing order."""

    L[:] = _quicksort_1(L)

############ Quicksort 2 ############

def _partition_2(L, i, j):
    """Rearrange L[i:j] so that items < L[i] are at the beginning and items
    >= L[i] are at the end, and return the new index for L[i]."""

    v = L[i]
    k = i + 1
    j -= 1
    while k <= j:
        if L[k] < v:
            k += 1
        else:
            L[k], L[j] = L[j], L[k]
            j -= 1

    L[i], L[j] = L[j], L[i]
    return j

def _quicksort_2(L, i, j):
    """Sort L[i:j] by partitioning it around the first item, then recursing."""

    if i < j:
        pivot = _partition_2(L, i, j)
        _quicksort_2(L, i, pivot)
        _quicksort_2(L, pivot + 1, j)

def quicksort_2(L):
    """Sort list L in non-decreasing order."""

    _quicksort_2(L, 0, len(L))
