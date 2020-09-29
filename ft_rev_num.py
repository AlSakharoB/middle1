def ft_rev_num(number):
    r = 0
    if number > 0:
        while number > 0:
            r = (r * 10) + (number % 10)
            number = number // 10
        return r
    else:
        number *= -1
        while number > 0:
            r = (r * 10) + (number % 10)
            number = number // 10
        return -r