def insert_sort(li):
    for i in range(1, len(li)):  # i represents the index of token card
        tmp = li[i]
        j = i - 1  # j represents the index of card in hand

        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = tmp

    return li


if __name__ == "__main__":
    import random

    li = [i for i in range(10)]
    random.shuffle(li)
    print(li)
    li = insert_sort(li)
    print(li)
