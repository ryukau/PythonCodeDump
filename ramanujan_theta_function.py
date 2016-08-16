"""
https://en.wikipedia.org/wiki/Ramanujan_theta_function
"""

import cmath


# 素朴な実装。
# OverflowError が出る。
def ramanujanThetaFunction(a, b):
    if abs(a * b) >= 1:
        return None
    sum = 0
    for n in range(-100, 100):
        n2 = n / 2
        aa = a**((n + 1) * n2)
        bb = b**((n - 1) * n2)
        sum += aa * bb
    return sum


print(ramanujanThetaFunction(0.1 + 0.1j, 1 + 0.5j))
