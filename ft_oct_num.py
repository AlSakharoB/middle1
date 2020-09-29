import ft_rev_num as ft


def ft_oct_num(number):
    oct = 1
    while number > 0:
        oct = (oct * 10) + (number % 8)
        number //= 8
    oct = ft.ft_rev_num(oct)
    oct //= 10
    return oct

