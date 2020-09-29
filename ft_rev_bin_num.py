def ft_pow(number, stepen):
    result = 1
    stepen2 = 0
    while stepen2 < stepen:
        stepen2 += 1
        result *= number
    return result


def ft_rev_bin_num(number):
    dec = 0
    stepen = -1
    while number > 0:
        stepen += 1
        dec = dec + (number % 10) * ft_pow(2, stepen)
        number //= 10
    return dec



