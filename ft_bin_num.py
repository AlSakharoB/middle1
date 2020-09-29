import ft_rev_num as ft


def ft_bin_num(number):
    bin = 1
    while number > 0:
        bin = (bin * 10) + (number % 2)
        number //= 2
    bin = ft.ft_rev_num(bin)
    bin //= 10
    return bin



