def rob(numbers: list) -> int:
    """House Robber
    You are a professional robber planning to rob houses along a street. Each
    house has a certain amount of money stashed, the only constraint stopping you
    from robbing each of them is that adjacent houses have security system
    connected and it will automatically contact the police if two adjacent houses
    were broken into on the same night.

    Given a list of non-negative integers representing the amount of money of
    each house, determine the maximum amount of money you can rob tonight without
    alerting the police.

    Example 1:
    Input: [1, 2, 3, 1]
    Output: 4
    Explanation:
        Rob house 1 (money = 1) and then rob house 3 (money = 3).
        Total amount you can rob = 1 + 3 = 4.

    Example 2:
    Input: [2, 7, 9, 3, 1]
    Output: 12
    Explanation:
        Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
        Total amount you can rob = 2 + 9 + 1 = 12.
    """

    if not numbers:
        return 0
    elif len(numbers) < 3:
        return max(numbers[0], numbers[-1])

    money = [numbers[0], max(numbers[0], numbers[1])]
    for i in range(2, len(numbers)):
        money.append( max((money[i-2] + numbers[i]), money[i-1]) )
    return money[-1]


if __name__ == "__main__":
    print(rob([2, 7, 9, 3, 1]))
