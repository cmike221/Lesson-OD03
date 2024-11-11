def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Выбор опорного элемента (pivot)
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного
    return quick_sort(left) + middle + quick_sort(right)  # Рекурсивный вызов


# Пример использования
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Исходный массив:", data)
    sorted_data = quick_sort(data)
    print("Отсортированный массив:", sorted_data)
