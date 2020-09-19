def productExceptSelf(numbers: list) -> list:
    """Product of Array Except Self
    Given an array numbers of n integers where n > 1, return an array output such
    that output[i] is equal to the product of all the elements of numbers except
    numbers[i].

    Example:
    Input:  [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

    Constraint: It's guaranteed that the product of the elements of any prefix
    or suffix of the array (including the whole array) fits in a 32 bit integer.

    Note: Please solve it without division and in O(n).

    Follow up:
    Could you solve it with constant space complexity? (The output array does not
    count as extra space for the purpose of space complexity analysis.)
    """

    N = len(numbers)
    output_arr = [1 for i in range(N)]
    
    for i in range(1, N):
        output_arr[i] = numbers[i -1] * output_arr[i -1]

    R = 1
    for i in range(N -1, -1, -1):
        output_arr[i] *= R
        R *= numbers[i]

    return output_arr


if __name__ == "__main__":
    result = productExceptSelf([1,2,3,4])
    print(result)
