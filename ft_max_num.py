def ft_max_num(number):
    maxnum = 0
    num = 0
    if number < 0:
        number = -number
    while number > 0:
        num = number % 10
        if num > maxnum:
            maxnum = num
        number //= 10
    return maxnum


