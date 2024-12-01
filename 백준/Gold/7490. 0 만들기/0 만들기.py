import sys
input = sys.stdin.readline

T = int(input())
cases = [int(input()) for _ in range(T)]
    

def dfs(idx, expr, n, results):
    if idx > n:  # 공백 제거하고 계산
        expr_clear = expr.replace(" ", "")
        if eval(expr_clear) == 0:
            results.append(expr)
        return
    dfs(idx+1, expr + " " + str(idx), n, results)
    dfs(idx+1, expr + "+" + str(idx), n, results)
    dfs(idx+1, expr + "-" + str(idx), n, results)

for case in cases:
    results = []
    dfs(2, "1", case, results)
    results.sort()
    print("\n".join(results))
    print()