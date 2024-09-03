from itertools import product

def solution(word):
    answer = 0
    words_list = []
    for i in range(1, 6):  # 길이가 1~5까지 가능
        for s in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            words_list.append(''.join(s))
        words_list.sort()
    return words_list.index(word) + 1