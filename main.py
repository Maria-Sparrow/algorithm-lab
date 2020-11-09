def find_speed_for_eat_bananas(piles, hours):
    """

    :param piles: array of bananas
    :param hours: the time during which the monkey must eat all the bananas
    :return: a value that satisfies the condition
    >>> find_speed_for_eat_bananas([3, 6, 7, 11], 8)
    4
    >>> find_speed_for_eat_bananas([30, 11, 23, 4, 20], 6)
    23
    >>> find_speed_for_eat_bananas([30, 11, 23, 4, 20], 5)
    30
    >>> find_speed_for_eat_bananas([4,9,28,43],7)
    15

    """
    all_bananas = max_speed = 0
    for count_of_pile in piles:
        all_bananas += count_of_pile
        if max_speed < count_of_pile:
            max_speed = count_of_pile
    min_speed = all_bananas // hours

    if len(piles) == hours:
        return max_speed
    return search_by_binary_tree(min_speed, max_speed, piles, hours)

def search_by_binary_tree(min_bananas, max_bananas, piles,hours):
    """

    :param min_bananas:
    :param max_bananas:
    :param hours:
    :param piles:
    :return:
    >>>  search_by_binary_tree(1, 31, [31, 11, 23, 4, 20], 6)
    23
    """
    while min_bananas < max_bananas:
        middle = (min_bananas + max_bananas) // 2

        if jackie_can_eat(piles, hours, middle):
            max_bananas = middle
        else:
            min_bananas = middle+1
    return min_bananas

def jackie_can_eat(piles, hours_can_eat,middle):
    """

    :param middle:
    :param piles:
    :param hours_can_eat:
    :return:
    >>> jackie_can_eat([3, 6, 7, 11], 8, 6)
    True
    >>> jackie_can_eat([3, 6, 7, 11], 8, 3)
    False
    """
    all_hours = 0
    for count_of_pile in piles:
        all_hours += count_of_pile // middle
        if count_of_pile % middle != 0:
            all_hours += 1
    return all_hours <= hours_can_eat


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
