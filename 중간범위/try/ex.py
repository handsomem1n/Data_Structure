class DListNode: #doublylistnode
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

def init(H, T):
    H.next = T
    T.prev = H

def print_list(H, T):
    p = H.next
    while p != T: # 꼬리노드 T 도달할떄까지
        print(f"[{p.data}] <=> ", end="")
        p = p.next
    print("\b\b\b\b ")

if __name__ == "__main__":
    H = DListNode()
    T = DListNode()
    init(H, T)
