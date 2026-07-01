# def solution(genres, plays):
#     play_times = {}  # key:장르, value:[(인덱스, 재생횟수)]
#     total = {}  # key:장르, value: 재생횟수
#     for i in range(len(genres)):
#         key = genres[i]
#         if key in play_times:
#             play_times[key] += [(i, plays[i])]
#             total[key] += plays[i]
#         else:
#             play_times[key] = [(i, plays[i])]
#             total[key] = plays[i]
#     answer = []
#     total = sorted(total.items(), key=lambda x:-x[1])  # 재생횟수 내림차순 정렬
#     for key in total:
#         genres_play = play_times[key[0]]
#         genres_play = sorted(genres_play, key=lambda x:-x[1])

#         for i in range(len(genres_play)):
#             if i == 2:
#                 break
#             else:
#                 answer.append(genres_play[i][0])
#     return answer

from collections import defaultdict
def solution(genres, plays):
    genres_dict = {}
    genres_idx = defaultdict(list)
    for i in range(len(genres)):
        genres_dict[genres[i]] = genres_dict.get(genres[i], 0) + plays[i]  # 장르별 재생 횟수
        genres_idx[genres[i]].append((plays[i], i))  # 재생횟수, idx

    # sorted: 리스트뿐만 아니라 반복 가능한 객체면 대부분 받을 수 있음
    # 재생 횟수 기준으로 정렬
    genres_sorted = sorted(genres_dict.keys(), key=lambda x: genres_dict[x], reverse=True)
    
    # genres_idx = {
    # "classic": [(500, 0), (150, 2), (800, 3)],
    # "pop": [(600, 1), (2500, 4)]
    # }
    answer = []
    for genre in genres_sorted:
        songs = genres_idx[genre]
        songs_sorted = sorted(songs, key=lambda x: (-x[0], x[1]))
        
        for times, idx in songs_sorted[:2]:
            answer.append(idx)
    return answer