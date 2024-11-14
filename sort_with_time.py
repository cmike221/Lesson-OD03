import time
import random


def bubble_sort(mas):
    n = len(mas)
    for run in range(n - 1):
        for i in range(n - 1 - run):
            if mas[i] > mas[i + 1]:
                mas[i], mas[i + 1] = mas[i + 1], mas[i]
    return mas


def quick_sort(s):
    if len(s) <= 1:
        return s

    element = s[0]
    left = list(filter(lambda i: i < element, s))
    center = [i for i in s if i == element]
    right = list(filter(lambda i: i > element, s))

    return quick_sort(left) + center + quick_sort(right)


def quick_sort2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Выбор опорного элемента (pivot)
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного
    return quick_sort(left) + middle + quick_sort(right)  # Рекурсивный вызов


def selection_sort(arr):
    # Проходим по всему списку
    for i in range(len(arr)):
        # Предполагаем, что первый элемент в неотсортированной части - это минимальный
        min_index = i
        # Ищем минимальный элемент в оставшейся части списка
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # Меняем местами найденный минимальный элемент с первым элементом в неотсортированной части
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Пример использования
if __name__ == "__main__":
    # Создание списка из 1000 случайных чисел от 1 до 1000
    data = [random.randint(1, 1000) for _ in range(1000)]

    print("Исходный массив:", data)

    # Измерение времени выполнения
    start_time = time.time()  # Запоминаем время начала
    sorted_data = insert_sort(data)
    end_time = time.time()  # Запоминаем время окончания
    print("Отсортированный массив:", sorted_data)
    print("Время выполнения Сортировка вставками: {:.6f} секунд".format(end_time - start_time))

    # Измерение времени выполнения
    start_time = time.time()  # Запоминаем время начала
    sorted_data = bubble_sort(data)
    end_time = time.time()  # Запоминаем время окончания
    print("Отсортированный массив:", sorted_data)
    print("Время выполнения Сортировка пузырьком: {:.6f} секунд".format(end_time - start_time))

    # Измерение времени выполнения
    start_time = time.time()  # Запоминаем время начала
    sorted_data = selection_sort(data)
    end_time = time.time()  # Запоминаем время окончания
    print("Отсортированный массив:", sorted_data)
    print("Время выполнения Сортировка выбором: {:.6f} секунд".format(end_time - start_time))

    # Измерение времени выполнения
    start_time = time.time()  # Запоминаем время начала
    sorted_data = quick_sort(data)
    end_time = time.time()  # Запоминаем время окончания
    print("Отсортированный массив 1:", sorted_data)
    print("Время выполнения Быстрая сортировка : {:.6f} секунд".format(end_time - start_time))

    # Измерение времени выполнения
    start_time = time.time()  # Запоминаем время начала
    sorted_data = quick_sort2(data)
    end_time = time.time()  # Запоминаем время окончания
    print("Отсортированный массив 2:", sorted_data)
    print("Время выполнения Быстрая сортировка 2: {:.6f} секунд".format(end_time - start_time))

    # Измерение времени выполнения
    start_time = time.time()  # Запоминаем время начала
    sorted_data = insert_sort(data)
    end_time = time.time()  # Запоминаем время окончания
    print("Отсортированный массив:", sorted_data)
    print("Время выполнения Сортировка вставками: {:.6f} секунд".format(end_time - start_time))
