# 난수
from random import *


class Node:
    def __init__(self, data):
        self.data = data
        self.link = None


class LinkedList:  # 단일
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:  # 비어있다면
            self.head = Node(data)  # 새로운 노드를 생성해서 head로 설정
        else:  # 안비어있다면
            node = self.head # 현재의 head를 시작점으로 설정
            while node.link:  # 다음노드가 존재할때까지 반복
                node = node.link # 다음으로
            node.link = Node(data) #현재 node는 리스트의 마지막 노드를 가리나까 이 노드의 link에 새 노드를 생성하여 할당함으로써, 연결 리스트의 마지막에 새 노드를 추가


class Term:  # 항
    def __init__(self, coef, expo):
        self.coef = coef
        self.expo = expo


class Polynomial(LinkedList):  # 상속
    def read(coef, exp):  # 항읽고 저장
        while True:
            # coef, expo = map(int, int)
            P1.Term.expo = map(self.coef, self.exp)
            if coef != 0:
                self.append(Term(coef, expo))

    def display(self):
        node = self.head
        terms = []
        while node:
            term = node.data
            terms.append(f"{term.coef} x^{term.expo}")
            node = node.link
        return " + ".join(terms) + " +"

    def add(self, P2):  # 1+2
        result = Polynomial()
        nodeA = self.head
        nodeB = P2.head

        # 1
        while nodeA is not None and nodeB is not None:  # 비지않, 비지않
            termA = nodeA.data
            termB = nodeB.data
            # 항비교
            if termA.expo > termB.expo:
                result.append(Term(termA.coef, termA.expo))
                nodeA = nodeA.link
            elif termA.expo < termB.expo:
                result.append(Term(termB.coef, termB.expo))
                nodeB = nodeB.link
            else:  # 더함
                coefsum = termA.coef + termB.coef
                if coefsum!= 0 : # not 0
                    result.append(Term(coefsum, termA.expo))
                nodeA = nodeA.link
                nodeB = nodeB.link
        # 2-1
        while nodeA is not None:
            termA = nodeA.data
            result.append(Term(termA.coef, termA.expo))
            nodeA = nodeA.link
        # 2-2
        while nodeB is not None:
            termB = nodeB.data
            result.append(Term(termB.coef, termB.expo))
            nodeB = nodeB.link

        return result


if __name__ == "__main__":
    P1 = Polynomial()
    P2 = Polynomial()

    for i in range(5):
        P1.makePoly(randrange(-5, 5), randint(0, 5))
        P2.makePoly(randrange(-5, 5), randint(0, 5))

    print('Poly 1: ', end='')
    P1.dispaly()
    print('Poly 2 : ', end='')
    P2.display()

    P3 = Polynomial()
    P3.polyAdd(P1, P2)
    print('Poly 3 : ', end='')
    P3.display()
