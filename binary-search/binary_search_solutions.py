def binarySearch(value_list, item):
    """Binary search algorithm uses a divide and conquer technique to search
    a sorted list for an item. First you take the midpoint of the list, if
    the target value is higher you take the upper half, if lower you take the
    lower half and start the process again."""
    if len(value_list) < 1:
        return -1
    lower = 0
    upper = len(value_list)
    while lower < upper:
        x = lower + (upper - lower) // 2
        val = value_list[x]
        if item == val:
            return x
        elif item > val:
            if lower == x:
                return -1
            lower = x
        elif item < val:
            upper = x