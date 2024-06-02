class SortedArraySet:
    def __init__( self, capacity=10 ):
        self.capacity = capacity
        self.array = [None]*capacity
        self.size = 0

    def isEmpty(self):
        return self.size == 0


    def isFull(self):
        return self.size == self.capacity


    def __str__(self) : # MyArray 클래스의 인스턴스를 생성하고 print() 함수를 사용하여 출력하면, __str__ 메서드가 자동으로 호출되어 객체의 array 속성을 문자열로 변환합니다.
        return str(self.array[:self.size])

    # 이진탐색 사용 가능 ***
    def contains(self, e) :
        for i in range(self.size) :
            if self.array[i] == e : # 'e'가 아님
                # return 1
                return True
        # return 0
        return False
        
    def append(self, e) :
        # if self.array.contains(e) == False :
        #     return
        self.array[self.size] = e
        self.size += 1
        

    # 코드 7.4: 정렬된 배열을 이용한 집합의 insert 연산
    # 요소들이 정렬된 상태를 유지해야 함
    def insert(self, e) :   # O(n) -> O(n)
        # if self.array.contains(e) : return
        # self.contains(e)가 사용되는 이유는 contains 메서드가 SortedArraySet 클래스의 인스턴스 메서드로 정의되었기 때문입니다.
        
        if self.contains(e) or self.isFull(): # 가득찼거나 이미 있으면 안됨.
            return
        
        self.array[self.size] = e
        self.size +=1
        #정렬해야함 - 리버스버블로함
        for i in range(self.size-1, 0 ,-1) :
            # if self.array[i] > self.array[i-1] :
            #     self.array[i],self.array[i-1] = self.array[i-1] , self.array[i] 
            if self.array[i] >= self.array[i-1] :
                break
            self.array[i],self.array[i-1] = self.array[i-1] ,self.array[i] 
        
    def delete(self, e) : # O(n) -> O(n)
        # 없거나 사이즈가0이면 삭제 자체를 못함
        if self.isEmpty() or not self.contains(e) :
            return

        # 삭제(index찾고,)
        # 핵심 : 이 리스트는 정렬된 리스트임 -> e가 있는 index를 찾아내는 방법은?
        i = 0
        while self.array[i] < e :
            i = i +1
        #삭제할 e의 값이 존재하는 index i를 찾음

        self.size -= 1

        while i < self.size :
            self.array[i] = self.array[i+1]
            i += 1


    # 코드 7.5: 정렬되지 않은 배열을 이용한 집합의 == 연산
    def __eq__(self, setB): # O(mn) ---> O(n+m)
        # 두 집합의 원소의 갯수가 같아야함
        if self.size != setB.size :
            return False
        # 같은 원소를 가져야 함 -> 정렬되어 있으므로 -> a[i] == b[i]
        for i in range(self.size ):
            if self.array[i] == setB.array[i] :
                return True
        return False


    # 코드 7.6: 정렬된 배열을 이용한 집합의 union 연산
    def union(self, setB):  # O(mn) -> O(n+m)
        # 합집합이라는 새로운 집합 생성
        setC_union = SortedArraySet()
        # 사이즈 = a.size + b.size - 중복갯수 but 굳이 선언해둘필요는없음
        # setC.size = self.size + setB.size - 
        i,j = 0,0
        while i< self.size and j < setB.size :
            a = self.array[i]
            b = setB.array[j]
            if a == b :
                setC_union.append(a) # b도가능
                i+= 1 #b넣을 시 j +=1
                j+=1
            elif a <b:
                setC_union.append(a)
                i+= 1
            elif a >b:
                setC_union.append(b)
                j+=1
            #여기까지 하면, a와 b 중 하나는 c에 다 들어갔다. 나머지를 위해 아래와 같은 코드
        while i < self.size :
            setC_union.append(self.array[i]) # append(a)가 아님
            i+=1
        while j < setB.size :
            setC_union.append(setB.array[j])
            j+=1
        return setC_union
    '''
    이 코드는 intersect()에 대하여 O(mn)의 Complexity를 가짐. 정렬되어있다는 특성을 고려하지 않았기때문임.

    # 도전 코딩!
    def intersect(self, setB):  # O(mn) -> O(n+m)
        # 교집합 생성
        setC = SortedArraySet()
        #교집합 찾기 - 정렬되어있는 코드이므로 for 문돌려가며 찾지않아도 된다.
        for i in range(self.size) :
            a = self.array[i]
            if setB.contains(a)  == True :
                setC.append(a)
        return setC
    '''

    def intersect( self, setB ):  # O(mn) -> O(n+m) / 정렬되어있다는 특성을 활용함.
        setC_intersect = SortedArraySet()
        i = 0
        j = 0
        while i < self.size and j < setB.size :
            a = self.array[i]
            b = setB.array[j]
            if a == b :
                setC_intersect.append(a)
                i += 1
                j += 1
            elif a < b: 
                i += 1
            else :
                j += 1

        return setC_intersect

    # 도전 코딩!
    def difference(self, setB):  # O(mn) -> O(n+m)
        # 차집합 : self 집합에서 setB 집합의 요소를 제외한 요소들을 새로운 집합 setC(a-b)
        setC_diff = SortedArraySet()
        i,j= 0,0

        while i< self.size and j < setB.size :
            a = self.array[i]
            b = setB.array[j]
            if a==b:
                i+=1
                j+=1
            elif a<b:
                setC_diff.append(a)
                i+=1
            elif a>b:
                j+=1
        return setC_diff



if __name__ == "__main__":
    import random
    setA = SortedArraySet()
    setB = SortedArraySet()
    for i in range(5): 
        setA.insert(random.randint(1,9))
        setB.insert(random.randint(1,9))

    print('Set A:', setA)
    print('Set B:', setB)
    print('A U B:', setA.union(setB))
    print('A ^ B:', setA.intersect(setB))
    print('A - B:', setA.difference(setB))

