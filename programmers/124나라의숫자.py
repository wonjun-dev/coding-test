inputs = [n for n in range(1, 11)]


def solution(n):
    # 시간 초과
    import math
    from itertools import product

    lower = math.log(1 + (2 / 3 * n), 3)
    k = math.ceil(lower)  # k 자리수
    if k == 0:
        k = 1
    offset = int(-3 / 2 * (1 - 3 ** (k - 1)))

    m = n - offset

    arr = ["1", "2", "4"]
    nums = list(product((arr), repeat=k))
    answer = list(nums[m - 1])
    answer = "".join(answer)

    return answer


def change124(n):
    num = ["1", "2", "4"]
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


import time

s = time.time()
for n in inputs:
    print(solution(n))
time1 = time.time() - s

s = time.time()
for n in inputs:
    print(change124(n))
time2 = time.time() - s


print(time1 / time2)
