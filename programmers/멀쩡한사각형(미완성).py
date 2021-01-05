# 시간 초과
input1 = [8, 12]


def solution(w, h):
    import math

    gcd = math.gcd(w, h)
    unit_w = int(w // gcd)
    unit_h = int(h // gcd)
    unit_area = unit_w * unit_h

    unit_usable = 0
    for x in range(1, unit_w):
        y = -(unit_h / unit_w) * x + unit_h
        unit_usable += math.floor(y)
    unit_usable *= 2

    unit_unusable = unit_area - unit_usable

    unusable = unit_unusable * (w // unit_w)

    answer = w * h - unusable
    return answer


print(solution(input1[0], input1[1]))