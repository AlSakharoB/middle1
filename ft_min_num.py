def ft_min_num(number):
    minnum = 9
    num = 0
    if number < 0:
        number = -number
    while number > 0:
        num = number % 10
        if num < minnum:
            minnum = num
        number //= 10
    return minnum