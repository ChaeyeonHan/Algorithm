def solution(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            # 스택이 비어있을 때
            if not stack:
                return False
            stack.pop()

    return len(stack) == 0