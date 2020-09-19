def arrayMaxConsecutiveSum2(numbers: list) -> int:
    """Array Max Consecutive Sum 2
    Given an array of integers, find the maximum possible sum you can get from
    one of its contiguous subarrays. The subarray from which this sum comes must
    contain at least 1 element.

    Example:
    For numbers = [-2, 2, 5, -11, 6], the output should be
    arrayMaxConsecutiveSum2(numbers) = 7.

    The contiguous subarray that gives the maximum possible sum is [2, 5], with
    a sum of 7.

    Input/Output:
    - [execution time limit] 4 seconds (py3)
    - [input] An array of integers.
      Guaranteed constraints:
      3 ≤ numbers.length ≤ 105,
      -1000 ≤ numbers[i] ≤ 1000.
    - [output] integer
      The maximum possible sum of a subarray within numbers.
    """
    current_sum = max_sum = numbers[0]
    for i in range(1, len(numbers)):
        current_sum = max(numbers[i] + current_sum, numbers[i])
        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == "__main__":
    nums = [-2, 2, 5, -11, 6]
    print(arrayMaxConsecutiveSum2(nums))
