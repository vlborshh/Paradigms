from typing import List

def binarySearch(arr: List[int], number: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == number:
            return mid
        elif arr[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return -1
arr = [1, 2, 4, 6, 10, 12]
print(f"В массиве: {arr}")
number = int(input("Введите элемент для поиска: "))
result = binarySearch(arr, number)
if result == -1:
    print("Элемент не найден!!!")
else:
    print(f"Элемент: {number} находится по индексу: {result}")