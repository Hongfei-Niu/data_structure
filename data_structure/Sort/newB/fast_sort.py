def partition(li, left, right):
    tmp = li[left]

    while left < right:
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]

        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)

# the time complexity worst is the O(n^2)

# digui take the space complexity for taking system RAM (the functions), and will take between O(logn) and O(n)

# li = [9, 8, 7, 6, 5, 4, 3, 2, 1]

