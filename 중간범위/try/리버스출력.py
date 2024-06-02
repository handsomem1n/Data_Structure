# Deque D와 Queue Q 초기화
D = [1, 2, 3, 4, 5, 6, 7, 8]
Q = []

# Deque D의 내용을 Q로 이동
while D:
    Q.append(D.pop(0))

# Queue Q의 내용을 Deque D의 앞쪽으로 추가
while Q:
    D.insert(0, Q.pop(0))

print(D)  # 결과: [8, 7, 6, 5, 4, 3, 2, 1]
