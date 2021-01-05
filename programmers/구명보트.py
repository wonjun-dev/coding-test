input1 = [[70, 50, 80, 50], 100]
input2 = [[70, 80, 50], 100]


def solution(people, limit):
    from collections import deque

    answer = 0

    people.sort()
    people = deque(people)

    while people:
        if len(people) == 1:
            people.pop()

        else:
            weight = people[0] + people[-1]
            if weight > limit:
                people.pop()

            else:
                people.pop()
                people.popleft()

        answer += 1

    return answer


print(solution(input2[0], input2[1]))