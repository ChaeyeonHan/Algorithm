def solution(sizes):
    # 더 긴쪽이 가로로 가게끔 명함을 돌려
    x, y = 0, 0
    for a, b in sizes:
        w = max(a, b)
        h = min(a, b)
        
        x = max(x, w)
        y = max(y, h)
    return x*y