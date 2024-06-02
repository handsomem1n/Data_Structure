from random import *

class Term: #항
    def __init__(self, coef, expo):
        self.coef = coef
        self.expo = expo

class Node: 
    def __init__(self, coef, expo):
        self.coef = coef
        self.expo = expo
        self.link = None

class Polynomial:
    def __init__(self):
        # 각 항의 계수와 차수를 저장하는 딕셔너리
        self.terms = {}

        # 난수를 5개 생성하여 다항식 초기화
        for _ in range(5):
            coefficient = random.randint(1, 10) # 예: 1부터 10 사이의 정수
            degree = random.randint(0, 10)      # 예: 0부터 10 사이의 정수
            
            if degree in self.terms:
                self.terms[degree] += coefficient
            else:
                self.terms[degree] = coefficient

        # 계수가 0
        self.terms = {k: v for k, v in self.terms.items() if v != 0}

    def display(self): #
        node = self.head
        terms = []
        while node:
            term = node.data
            terms.append(f"{term.coef} x^{int(term.expo)}")
            node = node.link
        return " + ".join(terms) + " +"    

    def __str__(self):
        # 다항식을 문자열 형태로 반환
        terms_list = [f"{coef}x^{deg}" for deg, coef in sorted(self.terms.items(), key=lambda x: x[0], reverse=True)]
        return " + ".join(terms_list)





# 테스트 코드

if __name__ == "__main__" :
    P1 = Polynomial()
    P2 = Polynomial()

    for i in range(5) :
        P1.makePoly(randrange(-5, 5), randint(0,5))

    print('Poly 1: ', end='') : P1.dispaly()
    print('Poly 2 : ', end = '') : P2.display()

    P3 = Polynomial()
    P3.polyAdd(P1, P2)
    print('Poly 3 : ', end = '') : P3.display()


# poly = Polynomial()
# print(poly)


from random import randint

class Node:
    def __init__(self, coef, expo):
        self.coef = coef
        self.expo = expo
        self.link = None

class Polynomial:
    def __init__(self):
        self.head = None
    
    def makePoly(self, coef, expo):
        # 계수의 절댓값이 50보다 크지 않고, 차수가 size보다 크지 않아야 함
        if abs(coef) > 50:
            return
        if expo < 0 or expo > 4: # Assuming size is 4 based on the example
            return

        newNode = Node(coef, expo)
        if not self.head:
            self.head = newNode
            return
        
        prev, current = None, self.head
        while current:
            if current.expo == expo:
                current.coef += coef
                return
            if current.expo < expo:
                if prev:
                    prev.link = newNode
                    newNode.link = current
                else:
                    newNode.link = self.head
                    self.head = newNode
                return
            prev, current = current, current.link
        prev.link = newNode

    def display(self):
        current = self.head
        result = []
        while current:
            result.append(f"{current.coef}x^{current.expo}")
            current = current.link
        return ' + '.join(result)

    def polyAdd(self, P, Q):
        p = P.head
        while p:
            self.makePoly(p.coef, p.expo)
            p = p.link

        q = Q.head
        while q:
            self.makePoly(q.coef, q.expo)
            q = q.link


if __name__ == "__main__":
    P1 = Polynomial()
    P2 = Polynomial()

    for _ in range(5):
        P1.makePoly(randint(-50, 50), randint(0, 4))
        P2.makePoly(randint(-50, 50), randint(0, 4))

    print(f'Poly 1 : {P1.display()}')
    print(f'Poly 2 : {P2.display()}')

    P3 = Polynomial()
    P3.polyAdd(P1, P2)
    print(f'Poly 3 : {P3.display()}')

