input1 = [[93, 30, 55], [1, 30, 5]]
input2 = [[95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]]


def solution(w, h):
    import math

    answer = []

    prev_remain = 0
    for p, s in list(zip(w, h)):
        remain = math.ceil((100 - p) / s)
        if remain > prev_remain:
            prev_remain = remain

    return answer


print(solution(input1[0], input1[1]))
# print(solution(input2[0], input2[1]))