import math

def najvecji_skupni_delitelj_gcd(m, n):
    return math.gcd(m, n)

def najvecji_skupni_delitelj_moj(m, n):
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

print(najvecji_skupni_delitelj_gcd(96, 45))
print(najvecji_skupni_delitelj_moj(96, 45))