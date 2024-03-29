def count_sort(li, max_count=100):
    """
    only for non-negative integer list
    :param li:
    :param max_count: max value in list or assume a large number
    """
    count = [0 for _ in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for i in range(val):
            li.append(ind)
