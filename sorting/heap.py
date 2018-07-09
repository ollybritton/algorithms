# coding=utf-8
"""Heap Sort"""
# Binary trees are represented as follows:
# [5,4,3,2,1,0,1]:
#       (5)
#      /   \
#    (4)   (3)
#   /   \  /  \
#  2    1 0   1

# Left = (i*2)+1
# Right = (i*2)+2
# Parent = (i-1)/2


def down_heap(ls, i=0):
    left = (i*2)+1
    right = (i*2)+2

    if left >= len(ls) and right >= len(ls):
        # Is a "leaf" (no children). Where the children should be is off the end of the list.
        # If it's a leaf, that leaf is already a heap, because it's the greatest of the (non-existant) children.
        return ls

    elif right >= len(ls) and left < len(ls):
        # Is an only child. We don't need to compare it with the other element.
        if ls[left] <= ls[i]:
            # If the child is smaller, swap it.
            ls[i], ls[left] = ls[left], ls[i]

        return ls

    else:
        # It's your bog-standard binary tree/node.
        smallest_child = right if ls[right] < ls[left] else left

        if ls[smallest_child] < ls[i]:
            ls[i], ls[smallest_child] = ls[smallest_child], ls[i]

            return down_heap(ls, smallest_child)

        return ls


def create_heap(ls, i=0):
    # Turns the entire list into a heap, not just fixing the element at the top.
    for i in range(len(ls)):
        i = len(ls) - i - 1

        ls = down_heap(ls, i)

    return ls


def remove_min(ls):
    ls = down_heap(ls)

    if len(ls) <= 1:
        return []

    ls[0] = ls.pop()

    return down_heap(ls)


def heap_sort(ls):
    # Sorts the list by exploiting the properties of the heap.
    ls = create_heap(ls)
    new_list = []

    while len(ls) >= 1:
        new_list.append(ls[0])
        ls = remove_min(ls)

    return new_list
