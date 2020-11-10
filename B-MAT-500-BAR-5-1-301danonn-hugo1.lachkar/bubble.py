from utils import print_res

def bubble(numbers):
    ret = 0
    for i in range(0, len(numbers) - 1):
        for j in range(0, len(numbers) - i - 1):
            if numbers[i] > numbers[i + 1]:
                numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            ret += 1
    print_res("Bubble sort:", ret)