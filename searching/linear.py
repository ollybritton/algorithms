def linear(xs, target):
    for i in range(len(xs)):
        if xs[i] == target:
            return i


print(linear([5, 4, 3, 2, 1], 1))
