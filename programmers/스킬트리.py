input1 = ["CBD", ["BACDE", "CBADF", "AECB", "BDA"]]


def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        valid_skill_tree = list(skill)
        for s in tree:
            if s in valid_skill_tree:
                if s == valid_skill_tree[0]:
                    valid_skill_tree.pop(0)
                else:
                    break

        else:
            answer += 1

    return answer


print(solution(input1[0], input1[1]))