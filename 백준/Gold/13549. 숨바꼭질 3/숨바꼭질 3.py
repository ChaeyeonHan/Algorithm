import sys
from collections import deque
input = sys.stdin.readline
cnt = [0] * 100001

def bfs(N, K):
    q = deque()
    q.append(N)
    while q:
        cur_position = q.popleft()
        if cur_position == K:
            return cnt[cur_position]
        for next_position in (cur_position*2, cur_position-1, cur_position+1):
            if next_position < 0 or next_position > 100000:
                continue
            if cnt[next_position]:
                continue
            if next_position == cur_position * 2:
                cnt[next_position] = cnt[cur_position]
            else:
                cnt[next_position] = cnt[cur_position] + 1
            q.append(next_position)

N, K = map(int, input().split())
print(bfs(N, K))