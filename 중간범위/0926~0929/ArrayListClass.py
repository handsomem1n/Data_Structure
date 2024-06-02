class ArrayList:
    
    def __init__(self, capacity = 100): # ArrayList 클래스의 생성자를 정의합니다. 클래스 객체를 만들 때 자동으로 호출되는 메서드입니다. capacity라는 선택적 인자를 사용하며 기본값은 100으로 설정
        self.capacity = capacity # 생성자에서 받은 capacity 값을 인스턴스 변수 self.capacity에 할당
        self.array = [None] * self.capacity # none은 안됨 / self.array는 실제 데이터를 저장하는 리스트입니다. 초기에는 모든 요소가 None으로 설정되며, 길이는 capacity만큼
        self.size = 0 # self.size는 현재 저장된 요소의 수를 나타내는 변수입니다. 초기에는 0입니다.

    def isEmpty(self) : #isEmpty라는 메서드를 정의합니다. 이 메서드는 ArrayList가 비어 있으면 True를, 그렇지 않으면 False를 반환합니다.
        return self.size == 0 # 저장된 요소의 수가 0인지 확인

    def isFull(self) :
        return self.size == self.capacity # 저장된 요소의 수가 최대 용량과 같은지 확인

    def insert(self, pos, e) : # (position) / 이 메서드는 pos 위치에 요소 e를 삽입
        # global size #global 필수
        if not (self.isFull() and 0 <= pos <= self.size) : # ArrayList가 꽉 차 있지 않고, 삽입하려는 위치가 유효한 범위 내에 있는지 확인
            for i in range(self.size, pos, -1): # pos 위치에 삽입하기 위해 해당 위치부터 오른쪽의 모든 요소를 오른쪽으로 한 칸씩 이동
                self.array[i] = self.array[i-1]
            self.array[pos] = e
            self.size += 1
        else :  
            print("overflow or invalid position")

    def replace(self, pos, e) : # pos 위치의 요소 값을 e로 변경
        if (0<= pos < self.size) :
            self.array[pos] = e
        else : pass

    def delete(self, pos) :
        if not self.isEmpty() and 0 <= pos <= self.size:
            e = self.array[pos]
            for i in range(pos, self.size-1):
                self.array[i] = self.array[i+1]
            self.size -= 1
        else:
            print("overflow or invalid position")

    def display(self):
        for i in range(self.size):
            print(self.array[i], end = ' ')
        print()

if __name__ == '__main__':
    L1 = ArrayList(10)
    L2 = ArrayList(7)

    L1.insert(0, 10)
    L1.insert(0, 20)
    L1.insert(L1.size, 30)
    L1.insert(1, 40)
    L1.display()

    L2.insert(0, 'B')
    L2.insert(0, 'A')
    L2.insert(1, 'C')
    L2.display()


