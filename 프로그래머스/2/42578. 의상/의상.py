# # def solution(clothes):
# #     dict = {}
# #     for name, type in clothes:
# #         dict[type] = dict.get(type, 0) + 1
# #     answer = 1
# #     for type in dict:
# #         answer *= (dict[type]+1)
# #     return answer-1


# from collections import defaultdict

# def solution(clothes):
#     cloth_dict = defaultdict(int)
#     answer = 1
#     for name, type in clothes:
#         cloth_dict[type] += 1
#     for value in cloth_dict.values():
#         answer *= (value+1)
#     # print(cloth_dict)
#     return answer-1

def solution(clothes):
    cloth_dict = {}
    for a, b in clothes:
        cloth_dict[b] = cloth_dict.get(b, 0) + 1
    
    cnt = 1
    for val in cloth_dict.values():
        cnt *= (val+1)
    return cnt-1