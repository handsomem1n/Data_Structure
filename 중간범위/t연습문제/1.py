# 난수
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList: # 단일
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.link:
                node = node.link
            node.link = Node(data)

class Term: #항
    def __init__(self, coef, expo):
        self.coef = coef
        self.expo = expo







class SparsePoly(LinkedList): #상속
    def read(self): # 항읽고 저장
        while True:
            coef, expo = map(float, input("계수, 차수 입력(종료 조건 : -1) : ").split())
            if coef == -1 and expo == -1:
                break
            if coef != 0:
                self.append(Term(coef, expo))








    def display(self):
        node = self.head
        terms = []
        while node:
            term = node.data
            terms.append(f"{term.coef} x^{int(term.expo)}")
            node = node.link
        return " + ".join(terms) + " +"

    def add(self, polyB):
        result = SparsePoly()
        nodeA = self.head
        nodeB = polyB.head

        while nodeA is not None and nodeB is not None:
            termA = nodeA.data
            termB = nodeB.data

            if termA.expo > termB.expo:
                result.append(Term(termA.coef, termA.expo))
                nodeA = nodeA.link
            elif termA.expo < termB.expo:
                result.append(Term(termB.coef, termB.expo))
                nodeB = nodeB.link
            else:
                new_coef = termA.coef + termB.coef
                if new_coef:
                    result.append(Term(new_coef, termA.expo))
                nodeA = nodeA.link
                nodeB = nodeB.link

        while nodeA is not None:
            termA = nodeA.data
            result.append(Term(termA.coef, termA.expo))
            nodeA = nodeA.link

        while nodeB is not None:
            termB = nodeB.data
            result.append(Term(termB.coef, termB.expo))
            nodeB = nodeB.link

        return result

# polyA = SparsePoly()
# polyA.read()
# print(f"입력 다항식 : {polyA.display()}")

# polyB = SparsePoly()
# polyB.read()
# print(f"입력 다항식 : {polyB.display()}")

# polyC = polyA.add(polyB)

# print(f"\nA = {polyA.display()}")
# print(f"B = {polyB.display()}")
# print(f"A+B = {polyC.display()}")



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

