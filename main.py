# Бинарный поиск - пример логаритмической сложности O(log n)
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # элемент найден
        elif arr[mid] < target:
            left = mid + 1  # искать в правой половине
        else:
            right = mid - 1  # искать в левой половине

    return -1  # элемент не найден

# Пример использования функции
arr = [1, 3, 5, 7, 9]
target = 7
result = binary_search(arr, target)
print(result)


# Сумма всех пар - пример квадратичной сложности O(n^2)
def sum_of_pairs(arr):
    """Функция для поиска суммы всех пар элементов в массиве.

    Args:
        arr (list): Входной массив чисел.

    Returns:
        list: Список сумм всех пар элементов.
    """
    n = len(arr)
    sums = []

    for i in range(n):
        for j in range(i + 1, n):
            sums.append(arr[i] + arr[j])

    return sums

# Общая сумма всех пар - пример квадратичной сложности O(n^2)
array = [1, 2, 3, 4]
result = sum_of_pairs(array)
print("Суммы всех пар элементов:", result)


def sum_of_pairs(arr):

    n = len(arr)
    total_sum = 0  # Переменная для хранения общей суммы

    for i in range(n):
        for j in range(i + 1, n):
            total_sum += arr[i] + arr[j]  # Добавляем сумму пары к общей

    return total_sum  # Возвращаем общую сумму

array = [1, 2, 3, 4, 5]
result = sum_of_pairs(array)
print("Общая сумма всех пар элементов:", result)


# Функция для умножения матриц - пример кубической сложности O(n^3)
def multiply_matrices(matrix1, matrix2):
    result = []
    m = len(matrix1)                # Количество строк в первой матрице
    n = len(matrix2[0])             # Количество столбцов во второй матрице
    p = len(matrix2)                # Количество строк во второй матрице

    for i in range(m):
        result.append([0] * n)      # Создаем строку результата с нулями
        for j in range(n):
            for k in range(p):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

# Пример использования функции
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

result = multiply_matrices(matrix_a, matrix_b)
print(result)

# Функция для вычисления чисел Фибоначчи - пример экспоненциальной сложности O(n^3)
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Пример использования функции
n = 10
result = fibonacci(n)
print(result)