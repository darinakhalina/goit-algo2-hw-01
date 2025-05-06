import random
from typing import List


def find_kth_smallest(numbers: List[int], k: int) -> int:
    if not 1 <= k <= len(numbers):
        raise ValueError(
            "Please provide k in the range from 1 to the length of the list."
        )

    def partition(start: int, end: int, pivot_idx: int) -> int:
        pivot_value = numbers[pivot_idx]
        numbers[pivot_idx], numbers[end] = numbers[end], numbers[pivot_idx]
        store_idx = start

        for i in range(start, end):
            if numbers[i] < pivot_value:
                numbers[store_idx], numbers[i] = numbers[i], numbers[store_idx]
                store_idx += 1

        numbers[end], numbers[store_idx] = numbers[store_idx], numbers[end]
        return store_idx

    left, right = 0, len(numbers) - 1
    target_index = k - 1

    while left <= right:
        pivot_idx = random.randint(left, right)
        final_pivot_idx = partition(left, right, pivot_idx)

        if final_pivot_idx == target_index:
            return numbers[final_pivot_idx]
        elif final_pivot_idx < target_index:
            left = final_pivot_idx + 1
        else:
            right = final_pivot_idx - 1

    raise RuntimeError("Quick select failed.")


if __name__ == "__main__":
    test = [8, 11, 5, 3, 20, 17]
    k = 4
    result = find_kth_smallest(test, k)
    print(f"Element number {k} in the sorted list {test} is - {result}")
