# Реализация алгоритма пирамидальной сортировки


# Построение кучи

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Сортировка

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Тестирование алгоритма пирамидальной сортировки

my_list = [12, 11, 13, 5, 6, 7]
print("Исходный массив:")
print(my_list)

heap_sort(my_list)

print("Отсортированный массив:")
print(my_list)
