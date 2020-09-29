def ft_len_num(num):
    count = 0
    if num < 0:
        num = -num
    while num > 0:
        count += 1
        num //= 10
    return count
