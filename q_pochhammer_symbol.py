"""
https://en.wikipedia.org/wiki/Q-Pochhammer_symbol
"""


def qPochhammer(a, q, n):
    if n <= 0:
        return 1
    product = 1 - a
    for k in range(1, n):
        product *= (1 - a * q**k)
    return product


# コンピュータで計算は無理。
def phi(q):
    return qPochhammer(q, q, infinity)


def binomialCoefficient(n, k):
    r = 1
    for i in range(1, k + 1):
        r *= n
        n -= 1
        r /= i
    return r


# このやり方ではだめ。
def mockModularOrder2A(q):
    if q <= 0:
        return 0
    if q == 1:
        return 1
    sum = 0
    qq = q * q
    for n in range(10):
        sum += q**(n + 1) * qPochhammer(-qq, qq, n) / qPochhammer(q, qq, n + 1)
    return sum

for i in range(10):
    print(mockModularOrder2A(i))
