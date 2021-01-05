board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]


def solution(board, moves):
    answer = 0
    stack = []

    for m in moves:
        for b in board:
            if b[m - 1] != 0:
                doll = b[m - 1]
                break
        else:
            break
        if stack and stack[-1] == doll:
            stack.pop(-1)
            answer += 2
            b[m - 1] = 0
        else:
            stack.append(doll)
            b[m - 1] = 0

    return answer


print(solution(board, moves))
