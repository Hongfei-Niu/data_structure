def sift(li, low, high):  # when chose the topk big number use the small root heap
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
        if j + 1 <= high and li[j + 1] < li[j]:  # if the right child is bigger
            j = j + 1  # j is the right child
        if li[j] < tmp:
            li[i] = li[j]
            i = j
            j = 2 * i + 1
        else:
            li[i] = tmp
            break
    else:
        li[i] = tmp


def topk(li, k):
    heap = li[:k]

    for i in range((k-2)//2, -1, -1):  # O(nlogn/2)
        sift(heap, i, k - 1)
    # finish establish the heap

    for i in range(k, len(li)):
        if li[i] > heap[0]:
            heap[0] = li[i]
            sift(heap, 0, k-1)


    for i in range(k - 1, -1, -1):  # O(nlogn)
        heap[0], heap[i] = heap[i], heap[0]
        sift(heap, 0, i - 1)
    return heap
