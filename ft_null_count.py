def ft_null_count(number):
    nullcount = 0
    num = 0
    if number < 0:
        number = -number
    while number > 0:
        num = number % 10
        if num == 0:
            nullcount += 1
        number //= 10
    return nullcount
