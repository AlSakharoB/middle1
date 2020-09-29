def ft_multi_num(num):
    multi = 1
    if num < 0:
        num = -num
    while num > 0:
        multi *= num % 10
        num //= 10
    return multi

