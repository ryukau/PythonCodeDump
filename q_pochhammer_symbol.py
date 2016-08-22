"""
https://en.wikipedia.org/wiki/Q-Pochhammer_symbol
"""


def qPochhammer(a, q, n):
    if n < 1:
        return 1
    product = 1
    for k in range(n):
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


# これはだめ。
def mockModularOrder2A(q):
    if q <= 0:
        return 0
    if q == 1:
        return 1
    sum = 0
    qq = q * q
    for n in range(100):
        sum += (q**(n + 1)) * qPochhammer(-qq, qq, n) / \
            qPochhammer(q, qq, n + 1)
    return sum

for i in range(32):
    print(mockModularOrder2A(i))

print("qPochhammer Test:")
a = 4
q = 11
print("a = " + str(a))
print("q = " + str(q))
print("n = 1")
print(qPochhammer(a, q, 1) - (1 - a))
print("n = 2")
print(qPochhammer(a, q, 2) - (1 - a) * (1 - a * q**1))
print("n = 3")
print(qPochhammer(a, q, 3) - (1 - a) * (1 - a * q**1) * (1 - a * q**2))
print("n = 4")
print(qPochhammer(a, q, 4) - (1 - a) * (1 - a * q**1)
      * (1 - a * q**2) * (1 - a * q**3))
