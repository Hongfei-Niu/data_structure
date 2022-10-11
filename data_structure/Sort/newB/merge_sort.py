# if two sequence are sorted and merged to a new sequence.

# li1 = [2, 5, 7, 8, 9]; li2 = [3, 4, 6]

def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1

    while i <= mid:
        ltmp.append(li[i])

    while j <=high:
        ltmp.append(li[j])

    li[low:high+1] = ltmp


def merge_sort(li, low, high):
    if low < high:  # at least two element
        mid = low(low + high) // 2
        merge_sort(li, low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)

