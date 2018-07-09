def quicksort(ls):
    if len(ls) <= 1:
        return ls

    pivot = ls[0]

    lt, eq, gt = [], [], []

    for i in ls:
        if i < pivot:
            lt.append(i)

        elif i > pivot:
            gt.append(i)

        else:
            eq.append(i)

    return quicksort(lt) + eq + quicksort(gt)
