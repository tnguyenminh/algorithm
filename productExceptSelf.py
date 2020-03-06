def productExceptSelf(self, nums: List[int]) -> List[int]:
    """Product of Array Except Self
    Given an array nums of n integers where n > 1, return an array output such that
    output[i] is equal to the product of all the elements of nums except nums[i].

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

    N = len(nums)
    output_arr = [1 for i in range(N)]
    
    for i in range(1, N):
        output_arr[i] = nums[i -1] * output_arr[i -1]

    R = 1
    for i in range(N -1, -1, -1):
        output_arr[i] *= R
        R *= nums[i]

    return output_arr


result = productExceptSelf([1,2,3,4])
print (result)
