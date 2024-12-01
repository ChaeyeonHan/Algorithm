def solution(mats, park):
    mats.sort(reverse=True)
    for mat in mats:
        for j in range(len(park)-mat+1):
            for h in range(len(park[0])-mat+1):
                check = True
                # 돗자리 놓을 수 있는지 확인
                if park[j][h] == "-1" and j+mat <= len(park) and h+mat <= len(park[0]):
                    for k in range(mat): # 돗자리 내부 확인
                        for l in range(mat):
                            if park[j+k][h+l] != "-1":
                                check = False
                                break
                        if not check:
                            break
                    if check:
                        return mat
    return -1