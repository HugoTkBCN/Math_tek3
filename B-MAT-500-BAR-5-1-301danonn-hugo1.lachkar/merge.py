def merge_sort(left, right):
    sorted = []
    count = 0
    while (left and right):
        count += 1
        if (left[0] <= right[0]):
            sorted.append(left[0])
            left = left[1:]
        else:
            sorted.append(right[0])
            right = right[1:]
    sorted += left + right
    return (sorted, count)


def merge(numbers):
    ret = 0
    if ((len(numbers) <= 1)):
        return (numbers, ret)
    left = []
    right = []
    for i in range(0, len(numbers)):
        if (i >= len(numbers) // 2):
            right.append(numbers[i])
        else:
            left.append(numbers[i])
    left, tmp = merge(left)
    ret += tmp
    right, tmp = merge(right)
    ret += tmp
    sorted, tmp = merge_sort(left, right)
    ret += tmp
    return (sorted, ret)