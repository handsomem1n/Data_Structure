
def findadjacentnum(arr):
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        # 중간 원소와 다음 원소가 다르면 해당 위치를 반환
        if arr[mid] != arr[mid + 1]:
            return mid
        
        # 중간 원소와 앞 원소가 같다면, 다른 원소는 mid 이후에 위치한다.
        if arr[mid] == arr[0]:
            low = mid + 1
        # 그렇지 않다면, 다른 원소는 mid 이전에 위치한다.
        else:
            high = mid
            
    return -1  # 해당하는 원소가 없을 때 (이 경우는 문제 조건상 발생하지 않음)

class DListNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def init(H, T):
    H.next = T
    T.prev = H

def print_list(H, T):
    p = H.next
    while p != T:
        print(f"[{p.data}] <=> ", end="")
        p = p.next
    print("\b\b\b\b ")

if __name__ == "__main__":
    H = DListNode()
    T = DListNode()
    init(H, T)

    arr = [1, 1, 1, 2, 2, 2, 2]  # 예제 배열
    print(findadjacentnum(arr))
