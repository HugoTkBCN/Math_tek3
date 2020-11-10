def quicksort(numbers):
    ret = 0
    if (len(numbers) <= 1):
        return (numbers, ret)
    piv = numbers[0]
    left = []
    right = []
    middle = [piv]
    for i in range(1, len(numbers)):
        ret += 1
        if (numbers[i] < piv):
            right.append(numbers[i])
        else:
            left.append(numbers[i])
    ret_left = quicksort(left)
    ret_right = quicksort(right)
    return (ret_left[0] + middle + ret_right[0], ret + ret_left[1] + ret_right[1])