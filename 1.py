from typing import List, Tuple


def find_min_max(arr: List[int]) -> Tuple[int, int]:
    if not arr:
        raise ValueError("The array must not be empty")

    def min_max_recursive(left: int, right: int) -> Tuple[int, int]:
        if left == right:
            return arr[left], arr[left]

        if right == left + 1:
            if arr[left] < arr[right]:
                return arr[left], arr[right]
            else:
                return arr[right], arr[left]

        mid = (left + right) // 2
        min1, max1 = min_max_recursive(left, mid)
        min2, max2 = min_max_recursive(mid + 1, right)

        return min(min1, min2), max(max1, max2)

    return min_max_recursive(0, len(arr) - 1)


if __name__ == "__main__":
    numbers = [11, 4, 46, -10, 8, 0, 88, 23]
    minimum, maximum = find_min_max(numbers)
    print(f"Minimum value: {minimum}")
    print(f"Maximum value: {maximum}")
