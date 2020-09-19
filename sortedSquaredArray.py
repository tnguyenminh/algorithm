def sortedSquaredArray(numbers: list) -> list:
    """Squares of a Sorted Array
    Given an array of integers numbers sorted in non-decreasing order, return an
    array of the squares of each number, also in sorted non-decreasing order.

    Example 1:
        Input: [-4, -1, 0, 3, 10]
        Output: [0, 1, 9, 16, 100]

    Example 2:
        Input: [-7, -3, 2, 3, 11]
        Output: [4, 9, 9, 49, 121]

    Note:
        1 <= numbers.length <= 10000
        -10000 <= numbers[i] <= 10000
        numbers is sorted in non-decreasing order.
    """

    lenght = len(numbers)
    left = 0
    right = lenght - 1
    result = [0] * lenght

    for i in reversed(range(lenght)):
        if abs(numbers[left]) > numbers[right]:
            result[i] = numbers[left] * numbers[left]
            left += 1
        else:
            result[i] = numbers[right] * numbers[right]
            right -= 1
    return result


if __name__ == "__main__":
    print(sortedSquaredArray([-4,-1,0,3,10]))
