from CircularQueue import CircularQueue

class CircularDeque(CircularQueue) : #CircularQueue를 상속받은 CircularDeque
    def __init__(self, capacity = 10) :
        super().__init__(capacity) #자식 클래스 선언 전 부모클래스 먼저 선언


        #isEmpty, isFull(), display()
    def addFront(self, e):
        if not self.isFull():
            self.queue[self.front] = e
            self.front = (self.front - 1 + self.capacity) % self.capacity
        else : pass
    
    def addRear(self, e) :
        self.enqueue(e)

    def deleteFront(self) :
        self.dequeue()

    def deleteRear(self) :
        if not self.isEmpty() :
            e = self.queue[self.rear]
            self.rear = (self.rear - 1 + self.capacity) % self.capacity #반시계
            return e
        else : pass #비어있다면

    def getFront(self) :
        self.peak()

    def getRear(self) :
        if not self.isEmpty() :
            return self.queue[self.rear]
        else : pass
        
if __name__ == '__main__' :

    import random

    D = CircularDeque()
    for i in range(4) :
        D.addFront(random.randiant(65, 90)) # 65 ~ 90
    D.display()

    for i in range(3):
        D.addRear(random.radiant(65,90))
    D.display

    for i in range(2):
        D.deleteFront()
    D.display
    
    for i in range(2):
        D.deleteFront()
    D.display

