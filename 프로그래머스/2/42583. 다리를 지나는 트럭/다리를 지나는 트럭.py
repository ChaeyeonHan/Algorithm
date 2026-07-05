# from collections import deque
# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     bridge = deque([0]*bridge_length)  # 다리에 올라온 트럭 표시를 위한 덱
#     truck_weights = deque(truck_weights)

#     total = 0
#     while len(truck_weights):
#         time += 1
#         total -= bridge.popleft()
#         if total+truck_weights[0] <= weight:
#             total += truck_weights[0]
#             bridge.append(truck_weights.popleft())
#         else:
#             bridge.append(0)

#     time += bridge_length

#     return time


from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    time, total = 0, 0
    while len(truck_weights):
        time += 1
        total -= bridge.popleft()
        if total + truck_weights[0] <= weight:  # 무게 넘지 않는 경우
            total += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0) # 트럭 올리지 못했으니까 빈공간에 0 넣어줌
    time += bridge_length            
    return time