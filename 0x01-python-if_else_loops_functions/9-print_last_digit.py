#!/usr/bin/python3
def print_last_digit(num):
    if num >= 0:
        ans = num % 10
    else:
        ans = num % -10
        ans *= -1

    print("{:d}".format(ans), end='')
    return (ans)
