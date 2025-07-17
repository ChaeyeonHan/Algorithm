def solution(numbers):
    result = set()
    # 서로 다른 인덱스에 있는 두 수를 더해 만들 수 있는 모든 수를 배열에 오름차순으로
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            result.add(numbers[i]+numbers[j])
    return sorted(result)