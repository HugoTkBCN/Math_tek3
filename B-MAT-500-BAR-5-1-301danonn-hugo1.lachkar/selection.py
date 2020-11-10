from utils import print_res

def selection(numbers):
    ret = 0
    for x in range(0, len(numbers) - 1):
        min = x
        for y in range(x + 1, len(numbers)):
            if numbers[y] < numbers[min]:
                min = y
            ret += 1
        numbers[x], numbers[min] = numbers[min], numbers[x]
    print_res("Selection sort:", ret)