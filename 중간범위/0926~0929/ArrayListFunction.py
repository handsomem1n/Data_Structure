capacity = 100
array = [None] * capacity # none은 안됨
size = 0

def isEmpty() :
    return size == 0

def isFull() :
    return size == capacity

def insert(pos, e) : # position,
    global size #global 필수
    if not (isFull() and 0 <= pos <= size) :
        for i in range( size, pos, -1):
            array[i] = array[i-1]
        array[pos] = e
        size += 1
    else :
        print("overflow or invalid position")

def delete(pos):
    global size
    if not isEmpty() and 0 <= pos < size:
        e = array[pos]
        for i in range(pos, size - 1):
            array[i] = array[i+1]
        size -= 1
        return e
    else:
        print('overflow or invalid')

def findItem(e):
    for i in range(size):
        if array[i] == e:
            return i
    return -1

def display():
    for i in range(size):
        print(array[i], end = ' ')
    print()

def getEntry(self, pos):
    if (0<= pos < self.size):
        return self.array[pos]
    else :
        return None

if __name__ == '__main__' :
    insert(0, 'a')
    insert(1, 'b')
    insert(1, 'c')
    insert(3, 'd')
    display()

    delete(2)
    display()

    e = input('input item to delete : ')
    idx = findItem(e)
    if idx != -1:
        delete(idx)
        display()
