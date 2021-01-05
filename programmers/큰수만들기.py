input1 = ["1924", 2, "94"]
input2 = ["1231234", 3, "3234"]
input3 = ["4177252841", 4, "775841"]
input4 = ["999121", 2]


def solution(number, k):
    stack = []
    number = list(map(int, number))

    for num in number:
        while k > 0 and stack and stack[-1] < num:
            stack.pop(-1)
            k -= 1
        stack.append(num)

    stack = list(map(str, stack))
    if k > 0:
        stack = stack[:-k]

    return "".join(stack)


print(solution(input1[0], input1[1]))
print(solution(input2[0], input2[1]))
print(solution(input3[0], input3[1]))
print(solution(input4[0], input4[1]))
