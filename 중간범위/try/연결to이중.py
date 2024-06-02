class DListNode:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def init(H, T):
    H.next = T
    T.prev = H
    # 원형으로 만드는 부분
    H.prev = T
    T.next = H

# def print_list(H, T):
def print_list(H): #원형리스트이므로
    p = H.next
    # 원형 리스트이므로 T에 다시 돌아올 때까지 계속 순회
    while p != H:
        print(f"[{p.data}] <=> ", end="")
        p = p.next
    print("\b\b\b\b ")

def insert(H, T, pos, e):
    newNode = DListNode(e)
    current = H
    for _ in range(pos):
        current = current.next
        if current == H:
            break

    prev_node = current.prev
    prev_node.next = newNode
    newNode.prev = prev_node
    newNode.next = current
    current.prev = newNode

if __name__ == "__main__":
    H = DListNode()
    T = DListNode()
    init(H, T)

    insert(H, T, 1, 20)
    insert(H, T, 2, 30)
    insert(H, T, 3, 50)
    insert(H, T, 4, 10)
    insert(H, T, 5, 40)
    # print_list(H, T)
    print_list(H)
    
    # 추가된 테스트
    print(H.prev.data, T.next.data)
