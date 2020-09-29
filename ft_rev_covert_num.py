def ft_pow(number, stepen):
    result = 1
    stepen2 = 0
    while stepen2 < stepen:
        stepen2 += 1
        result *= number
    return result


def ft_rev_covert_num(number, notation):
    covnum = 0
    stepen = -1
    while number > 0:
        stepen += 1
        covnum = covnum + (number % 10) * ft_pow(notation, stepen)
        number //= 10
    return covnum


