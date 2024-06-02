class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top == None

    def push(self, data):
        newNode = Node(data)
        newNode.link = self.top
        self.top = newNode

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.isEmpty():
            return None
        data = self.top.data
        self.top = self.top.link
        return data

    def peek(self):
        if self.isEmpty():
            return None
        return self.top.data

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

# 테스트
strings = ["A man, a plan, a canal, Panama", "racecar", "hello"]
for s in strings:
    print(f"'{s}' is palindrome? {is_palindrome(s)}")
