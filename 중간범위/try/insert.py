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
    print("\b\b\b\b \n", end="")

def insert(H, T, pos, e):
    newNode = DListNode(e) # 새로운 노드 생성
    
    current = H # pos 위치로 이동
    for _ in range(pos):
        current = current.next # 만약 pos가 리스트의 길이보다 크다면, T(마지막 노드)까지만 이동
        if current == T:
            break

    # newNode를 current 전에 삽입
    prevnode = current.prev
    prevnode.next = newNode
    newNode.prev = prevnode
    newNode.next = current
    current.prev = newNode

if __name__ == "__main__":
    H = DListNode()
    T = DListNode()
    init(H, T)
    insert(H, T, 1, 10)
    insert(H, T, 1, 20)
    insert(H, T, 2, 30)
    insert(H, T, 4, 40)
    insert(H, T, 3, 50)
    print_list(H,T)