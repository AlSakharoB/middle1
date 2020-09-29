import ft_rev_num as ft


def ft_mirror_num(number):
    if number < 0:
        number = -number
    revnum = ft.ft_rev_num(number)
    if revnum == number:
        return True
    return False