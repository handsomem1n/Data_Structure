
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

def insertTail(H, T, pos, e):
    newNode = DListNode(e)
    current = T
    for _ in range(pos):
        current = current.prev
        if current == H:
            break

    next_node = current.next
    next_node.prev = newNode
    newNode.next = next_node
    newNode.prev = current
    current.next = newNode

if __name__ == "__main__":
    H = DListNode()
    T = DListNode()
    init(H, T)

    insertTail(H, T, 1, 10)
    insertTail(H, T, 3, 60)
    insertTail(H, T, 4, 50)
    print_list(H, T)
