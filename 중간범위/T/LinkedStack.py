# 코드 6.1: 단순연결노드 클래스
class Node:
    def __init__ (self, elem, link=None):
        self.data = elem 
        self.link = link

# 코드 6.2: 연결된 스택 클래스
class LinkedStack :
    def __init__( self ):
        self.top = None

    def isEmpty( self ):
        return self.top == None

    def push( self, item ):
        self.top = Node(item, self.top)

    def peek( self ):
        if not self.isEmpty():
            return self.top.data

    def pop( self ):
        if not self.isEmpty():
            data = self.top.data
            self.top = self.top.link
            return data

    # 코드 6.3: 연결된 스택의 전체 요소의 수 계산
    def size( self ):
        node = self.top
        count = 0
        while not node == None :
            node = node.link
            count += 1
        return count

    # 코드 6.4: 문자열 변환을 위한 str 연산자 중복
    def __str__(self):
        arr = []
        node = self.top
        while not node == None :
            arr.append(node.data)
            node = node.link
        return str(arr)
            
def is_palindrome(s):
    s = ''.join([char.lower() for char in s if char.isalnum()])  # 영문자와 숫자만 고려
    stack = LinkedStack()

    # 문자열의 절반을 스택에 푸시
    for char in s[:len(s)//2]:
        stack.push(char)

    # 짝수 길이의 문자열일 경우 중간 문자를 건너뜀
    start = len(s) // 2 if len(s) % 2 == 0 else len(s) // 2 + 1

    # 나머지 절반의 문자열을 스택에서 팝하면서 일치하는지 확인
    for char in s[start:]:
        if char != stack.pop():
            return False
    return True


#======================================================================
if __name__ == "__main__":
    # s = LinkedStack()             # 스택 객체를 생성

    # print("스택: ", s)
    # msg = input("문자열 입력: ")    # 문자열을 입력받음
    # for c in msg :                  # 문자열의 각 문자 c에 대해
    #     s.push(c)                   # c를 스택에 삽입

    # print("스택: ", s)

    # print("문자열 출력: ", end='')
    # while not s.isEmpty():          # 스택이 공백상태가 아니라면
    #     print(s.pop(), end='')      # 하나의 요소를 꺼내서 출력
    # print()
    # print("스택: ", s)

    strings = ["A man, a plan, a canal, Panama", "racecar", "hello"]
    for s in strings:
        print(f"'{s}' is palindrome? {is_palindrome(s)}")
