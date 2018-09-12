from time import sleep

DEBUG = True
WAIT_TIME = 0


def merge(ls1, ls2):
    new_list = []
    original_ls1 = ls1
    original_ls2 = ls2

    while True:
        if len(ls1) == 0:
            return new_list + ls2

        if len(ls2) == 0:
            return new_list + ls1

        x1, x2 = ls1[0], ls2[0]

        if x1 < x2:
            new_list.append(x1)
            del ls1[0]

        elif x1 > x2:
            new_list.append(x2)
            del ls2[0]

        else:
            new_list.append(x1)
            new_list.append(x2)
            del ls1[0]
            del ls2[0]

    return new_list


def split(ls):
    if len(ls) == 1:
        return ls

    left, right = ls[:int(len(ls)/2)], ls[int(len(ls)/2):]

    return [left, right]


def sort(ls):
    if DEBUG:
        sleep(WAIT_TIME)

    if len(ls) <= 1:
        return ls

    split_ls = split(ls)

    left = sort(split_ls[0])
    right = sort(split_ls[1])

    new_list = merge(left, right)

    return new_list


def merge_sort(ls):
    if len(ls) <= 1:
        return ls

    left, right = merge_sort(
        ls[:int(len(ls)/2)]), merge_sort(ls[int(len(ls)/2):])

    new_list = []
    ls1, ls2 = left, right
    original_ls1 = ls1
    original_ls2 = ls2

    while True:
        if len(ls1) == 0:
            return new_list + ls2

        if len(ls2) == 0:
            return new_list + ls1

        x1, x2 = ls1[0], ls2[0]

        if x1 < x2:
            new_list.append(x1)
            del ls1[0]

        elif x1 > x2:
            new_list.append(x2)
            del ls2[0]

        else:
            new_list.append(x1)
            new_list.append(x2)
            del ls1[0]
            del ls2[0]

    return new_list


print(merge_sort([83, 52, 69, 10, 120, 2, 49]))
