price1 = [4, 1, 4, 7, 6]
price2 = [13, 7, 3, 7, 5, 16, 12]
import numpy as np


def solution(price):
    price_len = len(price)
    result = np.array([-1 for _ in range(price_len)])

    for i in range(1, price_len):
        futre_price = np.zeros(price_len)
        futre_price[0:-i] = price[i:]

        diff = np.array(futre_price) - np.array(price)

        result[np.where((diff > 0) & (result == -1))] = i

    return list([int(x) for x in result])


print(solution(price1))
print(solution(price2))
