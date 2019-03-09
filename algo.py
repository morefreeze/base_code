# Algorithm code collections
def power(a, n, mod):
    a %= mod
    p = a
    ret = 1
    while n:
        if n % 2:
            ret = (ret * p) % mod
        p = (p * p) % mod
        n //= 2
    return ret
