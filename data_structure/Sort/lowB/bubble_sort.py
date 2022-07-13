def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                # print(li)
                exchange = True
        if not exchange:
            return li


def bubble_sort_test(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return li


if __name__ == "__main__":
    import random

    li = [i for i in range(10)]
    random.shuffle(li)
    print(li)
    li = bubble_sort(li)
    print(li)
