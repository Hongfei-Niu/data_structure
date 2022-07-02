def sift(li, low, high):
    """

    :param li: list
    :param low: the co-ordinate of the root
    :param high: the co-ordinate of the last element in the heap
    :return:
    """

    i = low  # i is the root when begin
    j = 2 * i + 1  # j is the left child

    tmp = li[low]  # take the root

    while j <= high:  # when there is number on j
        if j + 1 <= high and li[j + 1] > li[j]:  # if the right child is bigger
            j = j + 1  # j is the right child
        if li[j] > tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def heap_sort(li):
    n = len(li)

    for i in range((n - 2) // 2, -1, -1):  # O(nlogn/2)
        sift(li, i, n - 1)
    # finish establish the heap

    for i in range(n - 1, -1, -1):  # O(nlogn)
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)


if __name__ == "__main__":
    import heapq
    import random

    li = list(range(100))
    random.shuffle(li)

    print(li)
    heapq.heapify(li)  # establish the heap
    print(li)  # small root heap

    heapq.heappop(li)  # pop out the smallest value in list
