class CircularQueue :

    def __init__(self, capacity = 8):
        self.capacity = capacity
        self.queue = [None] * self.capacity
        self.front = self.rear = 0

    def isEmpty(self) :
        return self.front == self.rear
    
    def isFull(self) :
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, e) :
        if not self.isFull() :
            self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = e
        else :
            print('full')

    def dequeue(self) :
        if not self.isEmpty() :
            self.front = (self.front + 1) % self.capacity
            return self.queue[self.front]
        else :
            print('empty')

    def peek(self) :
        if not self.isEmpty() :
            return self.queue[(self.front+1) % self.capacity]
        else :
            print('empty')
    
    def display(self) :
        print('front : %d, rear : %d' %(self.front, self.rear))

        i = self.front
        
        while i != self.rear:
            i = (i+1 ) % self.capacity
            print('[%c]' %self.queue[i], end= ' ')


    
if __name__ == '__main__':
    Q = CircularQueue()
    Q.enqueue('A')
    Q.enqueue('B')
    Q.enqueue('C')
    Q.enqueue('D')
    Q.enqueue('E')


    print('dequeue -- > ', Q.dequeue())
    print('dequeue -- > ', Q.dequeue())
    print('dequeue -- > ', Q.dequeue())
    Q.display()