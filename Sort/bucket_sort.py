def bucket_sort(li, n=100, max_num=10000):
    """
    bucket_sort
    :param n: number of the buckets
    :param max_num: assuming max number in list
    :return:
    """
    buckets = [[] for _ in range(n)]  # create n buckets
    for var in li:
        i = min(var // (max_num // n), n-1)  # i means the buckets for var number
        buckets[i].append(var)

        # every time insert the number in bucket, sort it by bubble sort
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j],  buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break

    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)

    return sorted_li

# time: O(n + k) - O(n^2k), k=logm*logn: the average length of one bucket
# space: O(nk)
