def findDuplicate(lstNumber):
    """Find Duplicate Number

    Given an array lstNumber containing n + 1 integers where each integer is between
    1 and n (inclusive), prove that at least one duplicate number must exist.
    Assume that there is only one duplicate number, find the duplicate one.

    Example 1:
        Input: [1, 3, 4, 2, 2]
        Output: 2

    Example 2:
        Input: [3, 1, 3, 4, 2]
        Output: 3

    Note:
        You must not modify the array (assume the array is read only).
        You must use only constant, O(1) extra space.
        Your runtime complexity should be less than O(n2).
        There is only one duplicate number in the array, but it could be repeated more than once.

    Complexity Analysis: Floyd's Tortoise and Hare (Cycle Detection) Approach
        Time complexity : O(n)
        Space complexity : O(1)
    """

    # find the intersection point of the two runners
    tortoise = hare = lstNumber[0]
    while True:
        tortoise = lstNumber[tortoise]
        hare = lstNumber[lstNumber[hare]]
        if tortoise == hare:
            break

    # find the "entrance" to the cycle
    ptr1 = lstNumber[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = lstNumber[ptr1]
        ptr2 = lstNumber[ptr2]

    return ptr1

test = [3, 1, 3, 4, 2]
print(findDuplicate(test))