'''
List를 따름
up - head :
    1. 마지막 노드로 삽입 : append
    2. 부모노드와 비교
        부모가 클 때, : break
        자식이 클 때 : 교환
'''
# 마지막 노드로 삽입
def heappush(heap, n) :
    heap.append(n)
    i = len(heap) - 1 # 0번 인덱스를 사용하진 않으니 i = len - 1
    while i is not 1 : # 0번 인덱스를 사용하지 않으니 0까지 비교하지 않고, i != 1이다.
        pi = i // 2
        # 부모노드와 비교
        if heap[pi] >= n : # 부모가 클 때
            break
        # else # heap[pi] < n : # 자식이 클 때
        heap[i] = heap[pi]
        i = pi
    heap[i] = n


# 삭제연산의 주핵심동작은 1. 루트노드를 삭제하고 2. 완전이진트리 특성을 유지하기 위해 루트노드에서 부터 말단노드에서까지 내려오면서 비교하는 것임.
def heappop(heap) :
    size = len(heap) -1

    if size == 0 :
        return None

    pi = 1
    i = 2
    root = heap[1]  # 삭제할 루트 노드(우두머리)
    last = heap[size] # 말단

    while i <= size :
        if i<size and heap[i] < heap[i+1] : # i < size는 오른쪽 자식 노드가 존재하는지 확인합니다. / heap[i] < heap[i + 1]는 왼쪽 자식(heap[i])이 오른쪽 자식(heap[i + 1])보다 작은지 확인합니다.
            i +=1 # 만약 두 조건이 모두 참이면, 오른쪽 자식이 더 크므로, i를 증가시킴. 이는 곧 heap[pi] = heap[i]를 통해 오른쪽 자식을 선택하게 만들거임
        if last >= heap[i] : # 마지막 요소(last)가 선택된 자식 노드(heap[i])보다 크거나 같으면
            break
        # 첫 번째 if 문이 거짓인 경우 : 이는 오른쪽 자식 노드가 존재하지 않거나, 왼쪽 자식이 오른쪽 자식보다 크거나 같은 경우입니다. 이 경우, i는 증가되지 않으며, 왼쪽 자식이 선택됩니다.
        # 두 번째 if 문이 거짓인 경우 : 이는 '마지막 요소'(last)가 현재 선택된 자식 노드(heap[i])보다 작은 경우입니다. 즉, 마지막 요소를 현재 노드의 위치로 옮겨야 하며, 반복문은 계속 진행됩니다.

        # 결국, 두 조건문이 모두 거짓일 경우, last는 선택된 자식 노드(heap[i])보다 작으므로, 현재 노드(heap[pi])에 선택된 자식 노드의 값을 할당하고, 다음 자식 노드로 내려가는 과정을 계속합니다. 

        heap[pi] = heap[i] # 선택된 자식 노드의 값을 현재 노드(heap[pi])로 이동
        pi = i # pi를 자식 노드의 인덱스로 업데이트
        i *= 2 # i를 pi의 왼쪽 자식 인덱스로 업데이트

    heap[pi] = last # 마지막 요소를 적절한 위치(pi)에 배치
    heap.pop()
    return root # 삭제된 최대값(루트 노드)을 반환



            


if __name__ == "__main__":
    heap = [0] # 0번 인덱스를 사용하진 않지만, 그래도 공백으로 두진 않는다.