def ft_second_max_num(number):
    if number < 0:
        number = -number
    max1 = 0
    max2 = 0
    x = 0
    while number > 0:
        x = number % 10
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x
        number //= 10
    return max2
