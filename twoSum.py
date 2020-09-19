def twoSum(numbers: list, target: int) -> list:
    """Two Sum
    Given an array of integers, return indices of the two numbers uch that they
    add up to a specific target.

    You may assume that each input would have exactly one solution, and you
    may not use the same element twice.

    Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9, return [0, 1].
    """

    seen = dict()

    for index, num in enumerate(numbers):
        if num in seen:
            return [seen[num], index]
        seen[target - num] = index
    else:
        return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    targert = 9
    answer = twoSum(nums, targert)
    print(answer or "Not exist")
