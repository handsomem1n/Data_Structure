def find_min_max(A):
    min = A[0]
    max = A[0]
    for i in range(1, len(A)) :
        if max < A[i] : max = A[i]
        if min > A[i] : min = A[i]

    return (min, max) # 파이썬에서는 여러개의 값을 리턴할 수 있다.

data = [11, 22, 33, 44, 55]
find_min_max(data)
print(find_min_max(data))