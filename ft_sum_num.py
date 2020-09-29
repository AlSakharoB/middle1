def ft_sum_num(num):
    sum = 0
    if num < 0:
        num = -num
    while num > 0:
        sum += num % 10
        num //= 10
    return sum

