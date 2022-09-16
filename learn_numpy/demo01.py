def arr_add01(n):
    a = [i ** 3 for i in range(1, n + 1)]
    b = [i ** 2 for i in range(1, n + 1)]
    c = []
    for i in range(n):
        c.append(a[i] + b[i])
    return c


print(arr_add01(3))

import numpy as np


def arr_add02(n):
    a = np.arange(1, n + 1) ** 3
    b = np.arange(1, n + 1) ** 2
    return a + b


print(arr_add02(3))
