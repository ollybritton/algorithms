def bubble(xs):
    # Perform a bubble sort on list xs and return the sorted list.
    while True:
        unsorted = False
        print(xs)
        
        for i in range(len(xs) - 1):
            i += 1

            if xs[i] < xs[i-1]:
                xs[i], xs[i-1] = xs[i-1], xs[i]
                unsorted = True

            elif i == len(xs)-2 and unsorted == False:
                return xs
