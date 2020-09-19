def firstDuplicate(numbers: list) -> int:
    """First Duplicate
    Given an array that contains only numbers in the range from 1 to a.length,
    find the first duplicate number for which the second occurrence has the minimal
    index. In other words, if there are more than 1 duplicated numbers, return
    the number for which the second occurrence has a smaller index than the second
    occurrence of the other number does. If there are no such elements, return -1.

    Example
    For a = [2, 1, 3, 5, 3, 2], the output should be firstDuplicate(a) = 3.
    There are 2 duplicates: numbers 2 and 3. The second occurrence of 3 has a
    smaller index than the second occurrence of 2 does, so the answer is 3.
    For a = [2, 4, 3, 5, 1], the output should be firstDuplicate(a) = -1.

    Input/Output
    [input] array.integer a
    [output] integer

    The execution time limit is 4 seconds.

    Guaranteed constraints:
    1 <= a.length <= 10**5,
    1 <= a[i] <= a.length.
    """
    for i in range(len(numbers)):
        if numbers[abs(numbers[i])-1] < 0:
            return abs(numbers[i])
        else:
            numbers[abs(numbers[i])-1] = -numbers[abs(numbers[i])-1]

    return -1


if __name__ == "__main__":
    nums = [2, 1, 3, 5, 3, 2]
    print(firstDuplicate(nums))
