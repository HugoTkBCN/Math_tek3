from utils import print_res

def insertion(numbers):
    ret = 0
    for x in range(1, len(numbers)):
        y = x
        while (y > 0):
            ret += 1
            if (numbers[y - 1] <= numbers[y]):
                numbers[y], numbers[y - 1] = numbers[y - 1], numbers[y]
                y -= 1
            else:
                break
    print_res("Insertion sort:", ret)