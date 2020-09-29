import ft_rev_num as ft


def ft_covert_num(number, notation):
    covnum = 1
    while number > 0:
        covnum = (covnum * 10) + (number % notation)
        number //= notation
    covnum = ft.ft_rev_num(covnum)
    covnum //= 10
    return covnum










