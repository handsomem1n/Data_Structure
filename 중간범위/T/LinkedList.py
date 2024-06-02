# Linked List.
class Node:
    def __init__ (self, elem, next=None):
        self.data = elem 
        self.link = next

# 코드 6.5: 연결리스트 클래스
class LinkedList:
    # 리스트의 데이터: 생성자에서 정의 및 초기화
    def __init__( self ):
        self.head = None

    # 리스트의 연산: 클래스의 메소드
    def isEmpty( self ): return self.head == None
    def isFull( self ): return False

    def getNode(self, pos) :
        if pos < 0 : return None
        node = self.head
        while pos > 0 and node != None : # 시작위치부터 Pos번 링크를 따라 움직이면서 pos 위치의 노드에 도착
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos) :
        node = self.getNode(pos)
        if node == None:
            return None
        else : 
            return node.data

    def insert(self, pos, elem) :
        before = self.getNode(pos-1) # pos - 1위치의 노드를 먼저 구함
        if before == None :         # 맨 앞에 삽입함
            self.head = Node(elem, self.head)
        else :
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None :         # 맨 앞 노드를 삭제
            if self.head is not None :
                self.head = self.head.link
        elif before.link != None :
            before.link = before.link.link

    # 추가 연산들
    def size( self ) :
        node = self.head;
        count = 0;
        while node is not None :
            node = node.link
            count += 1
        return count

    def __str__( self ) :
        arr = []
        node = self.head
        while node is not None :
            arr.append(node.data)
            node = node.link
        return str(arr)
    

    def replace(self, pos, elem) :
        node = self.getNode(pos)
        if node != None : node.data = elem

    def find(self, val) :
        node = self.head;
        while node is not None:
            if node.data == val : return node
            node = node.link
        return node
#-------------승추
    def printForward(self):
        node = self.head
        while node is not None:
            print(node.data, end=" -> ")
            node = node.link
        print("None")

    def printReverseRecursive(self, node=None): # 재귀
        if node is None:
            node = self.head
        if node is not None:
            self.printReverseRecursive(node.link)
            print(node.data, end=" -> ")

    def printReverseIterative(self): # 순환
        stack = []
        node = self.head
        while node:
            stack.append(node.data)
            node = node.link

        while stack:
            print(stack.pop(), end=" -> ")


    def append(self, elem):
        if not self.head:  # 리스트가 비어 있을 경우
            self.head = Node(elem)
        else:
            node = self.head
            while node.link:  # 마지막 노드를 찾을 때까지 이동
                node = node.link
            node.link = Node(elem)

    def merge(self, otherList):
        # A가 비어 있으면, B를 그대로 A에 연결
        if not self.head:
            self.head = otherList.head
            otherList.head = None
            return

        # A의 맨 뒷부분 찾기
        node = self.head
        while node.link: # node.link 찾을떄까지
            node = node.link # 찾기
        
        # A의 맨 뒷부분에 B의 처음 연결
        node.link = otherList.head # a 다음으로 following하는 후속리스트를 연결해줌
        otherList.head = None #b는 비게됨

    

    



#======================================================================
if __name__ == "__main__":
    L = LinkedList()
    
    print("최초   ", L)
    L.insert(0, 10)
    L.insert(0, 20)
    L.insert(1, 30)
    L.insert(3, 40)
    L.insert(2, 50)
    print("삽입x5 ", L)
    L.delete(2)
    print("삭제(2)", L)
    L.delete(3)
    print("삭제(3)", L)
    L.delete(0)
    print("삭제(0)", L)

