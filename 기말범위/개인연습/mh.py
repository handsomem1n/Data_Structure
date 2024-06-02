# 코드 8.14: 최대힙의 삽입 알고리즘         참고 코드: ch08/MaxHeap.py
def heappush(heap, n) : # up heap
    heap.append(n) #넣어
    i = len(heap)-1
    while i != 1 :
        parent_i = i//2
        if n <= heap[parent_i] :
            break
        #elif n> heap[parent_i]:
        heap[i] = heap[parent_i]
        


# 코드 8.15: 최대힙의 삭제 알고리즘         참고 코드: ch08/MaxHeap.py
def heappop(heap) : # down heap
    size = len(heap) -1
    if size == 0 :
        return None
    
    root = heap[1]
    last = heap[size]

    parent_i = 1
    i=2

    while(i<=size):
        if i<size and heap[i]< heap[i+1] :
            i+=1
        if last >= heap[i] :
            break
        heap[parent_i] - heap[i]
        parent_i = i
        i*=2

if __name__ == "__main__":
    # 코드 8.16: 최대힙 테스트 프로그램
    data = [2, 5, 4, 8, 9, 3, 7, 3]		# 힙에 삽입할 데이터
    heap = [0]
    print("입력: ", data)
    for e in data :			    # 모든 데이터를 힙에 삽입
        heappush(heap, e)
        print("heap: ", heap[1:])

    print("삭제: ", heappop(heap))
    print("heap: ", heap[1:])
    print("삭제: ", heappop(heap))
    print("heap: ", heap[1:])

