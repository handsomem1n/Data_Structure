class ArraySet :
       
    def __init__(self, capacity = 100):
        self.capacity = capacity
        self.array = [None] * self.capacity # none은 안됨
        self.size = 0

    def isEmpty(self) :
        return self.size == 0

    def isFull(self) :
        return self.size == self.capacity
    
    def display(self):
        for i in range(self.size):
            print(self.array[i], end = ' ')
        print()

    def contains(self, e):
        for i in range(self.size) : #순차 탐색이니까 처음부터 끝까지 탐색
            if self.array[i] == e:
                return True
            
        return False
    
    def insert(self, e):
        if not self.contains(e) and not self.isFull() : #포함되어있지 않거나 / 배열에 집어넣을 수 잇는 공간이 존재한다면
            self.array[self.size]= e
            self.size += 1

    def delete(self, e) :
        for i in range(self.size):
            if self.array[i] == e :
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                return 
    def union(self, setB) : # 합집합
        setC = ArraySet()

        for i in range(self.size):
            setC.insert(self.array[i]) #집합 a의 모든 원소가 집합C로 이동함

        for i in range(setB.size):
            setC.insert(setB.array[i])

        return setC
    

    def intersect(self, setB): # 교집합
        setC = ArraySet()
        for i in range(self.size):
            if setB.contains(self.array[i]):
                setC.insert(self.array[i])

        return setC
    
    def difference(self, setB): #차집합
        setC = ArraySet()
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                setC.insert(self.array[i])

        return setC


if __name__ == '__main__':
    s = ArraySet()
    s.insert(10)
    s.insert(30)
    s.insert(20)
    s.insert(50)
    
    T = ArraySet()
    T.insert(10)
    T.insert(40)
    T.insert(50)
    T.insert(15)
    T.display()

    s.union(T).display()
    s.intersect(T).display()
    s.difference(T).display()