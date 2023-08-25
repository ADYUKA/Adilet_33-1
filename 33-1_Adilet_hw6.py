def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Before sorting:", numbers)
bubble_sort(numbers)
print("After sorting:", numbers)

print('----------------------------------------------')


def bin_search(nums, val):
    pos = -1
    ResultOk = False
    first = 0
    last = len(nums) - 1
    while first <= last:
        middle = (first + last) // 2
        if val == nums[middle]:
            first = middle
            last = first
            ResultOk = True
            pos = middle
            break
        else:
            if val > nums[middle]:
                first = middle + 1
            else:
                last = middle - 1

    if ResultOk:
        print(f'Элемент {val} найден! Индекс {pos}')
    else:
        print(f'Элемент {val} не найден(')


list1 = list(range(1, 26))
bin_search(list1, 22)
bin_search(list1, 15)
bin_search(list1, 43)
bin_search(list1, 28)
