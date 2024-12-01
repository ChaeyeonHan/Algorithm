import sys
input = sys.stdin.readline

N, K, P, X = map(int, input().split())

# 디스플레이 상태
ch = [
    [1, 1, 1, 0, 1, 1, 1],  # 0
    [0, 0, 1, 0, 0, 1, 0],  # 1
    [1, 0, 1, 1, 1, 0, 1],  # 2
    [1, 0, 1, 1, 0, 1, 1],  # 3
    [0, 1, 1, 1, 0, 1, 0],  # 4
    [1, 1, 0, 1, 0, 1, 1],  # 5
    [1, 1, 0, 1, 1, 1, 1],  # 6
    [1, 0, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1],  # 9
]

# 1이상 N이하가 되도록, LED 최소 1개, 최대 P개 반전 가능
# 현재 X층에 위치, 층수를 보여주는 디스플레이에 K자리의 수가 보임
def change(N, K, P, X, ch):
    result = 0
    for i in range(1, N+1):
        if i == X:
            continue
        cnt = 0
        from_num, to_num = X, i  # 현재 숫자, 비교 숫자
        
        for j in range(K):  # 자릿수
            for p in range(7):
                if ch[from_num%10][p] != ch[to_num%10][p]: # 각 자릿수의 7개의 세그먼트 비교
                    cnt += 1
            # 자릿수 이동
            from_num //= 10
            to_num //= 10
        if cnt <= P:
            result += 1
    return result

print(change(N, K, P, X, ch))