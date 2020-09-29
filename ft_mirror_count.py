import ft_mirror_num as ft


def ft_mirror_count(number):
    if number < 0:
        number = -number
    palcount = 0
    for i in range(1, number + 1):
        if ft.ft_mirror_num(i):
            palcount += 1
    return palcount