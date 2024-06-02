class ArrayStack:
    def __init__(self, capacity = 100):
        self.capapcity = capacity
        self.stack = [None] * self.capapcity
        self.top = -1

    def isEmpty(self) :
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capapcity - 1
    
    def push(self, e) :
        if not self.isFull() :
            self.top += 1
            self.stack[self.top]  = e # [top]이 아님을 주의
        else :
            print('overflow')

    def pop (self):
        if not self.isEmpty() :
            e = self.stack[self.top]
            self.top -= 1
            return e
        else :
            print('empty')

    def peek(self) :
        if not self.isEmpty() :
            return self.stack[self.top]
        else :
            print('empty')

    def size(self) :
        return self.top + 1
    
    def display(self) :
        print(self.stack[self.top::-1]) #top 부터 0번 index까지

if __name__ == '__main__':
    s = ArrayStack()

    str = input('input a string : ')

    for c in str :
        s.push(c)
    s.display()

    # print('after pop : %c' %s.pop())
    # s.display()
    
    # print('after peek : %c' %s.peek())
    # s.display()

    while not s.isEmpty() :
        print(s.pop(), end = ' ' )                

