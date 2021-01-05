input1 = "JEROEN"
input2 = "JAN"
input3 = "AAAJAAAAAAN"


def solution(name):
    import numpy as np

    target_number = np.array(list(map(ord, name)))
    init_number = np.array([65 for _ in range(len(name))])

    # up & down
    up = target_number - init_number
    down = init_number - target_number + 26
    stack = np.stack((up, down))
    vertical_move = np.min(stack, axis=0)

    # left & right
    left = np.array([vertical_move[i] for i in range(0, -len(name), -1)])
    right = np.array([vertical_move[i] for i in range(0, len(name), 1)])
    print(left, right)
    try:
        l = np.where(left != 0)[0][-1]
        r = np.where(right != 0)[0][-1]
        horizon_move = np.min((l, r))
    except:
        horizon_move = 0

    answer = np.sum(vertical_move) + horizon_move
    return int(answer)


print(solution(input1))
print(solution(input2))
print(solution(input3))