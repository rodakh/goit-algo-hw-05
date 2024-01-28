def binary_search_upper_bound(arr, target):
    left, right = 0, len(arr) - 1
    upper_bound = None
    iterations = 0

    while left <= right:
        iterations += 1
        mid = left + (right - left) // 2

        if arr[mid] == target:
            upper_bound = arr[mid]
            while mid + 1 < len(arr) and arr[mid + 1] == target:
                mid += 1
            upper_bound = arr[mid]
            break

        elif arr[mid] < target:
            left = mid + 1
        else:
            upper_bound = arr[mid]
            right = mid - 1

    return iterations, upper_bound


example_array = [1, 2, 4, 5, 6, 8, 9]
target_value = 7

iterations, result = binary_search_upper_bound(example_array, target_value)
print(f"Кількість ітерацій: {iterations}, Найближчий верхній дільник: {result}")
