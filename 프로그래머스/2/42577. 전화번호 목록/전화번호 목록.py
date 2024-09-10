def solution(phone_book):
    answer = True
    # 문자열 정렬한 뒤, 다음 문자열을 현재 문자열 길이만큼 슬라이싱하여 비교
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][0:len(phone_book[i])]:
            answer = False
            break
    return answer