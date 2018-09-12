def binary(xs, target):
    midway = len(xs)//2
    print(midway, xs)

    if xs[midway] == target:
        return True

    elif len(xs) == 1:
        return False

    elif xs[midway] < target:
        return binary(xs[midway:], target)

    elif xs[midway] > target:
        return binary(xs[:midway], target)


print(binary([1, 2, 3, 4, 5, 6], -12))
