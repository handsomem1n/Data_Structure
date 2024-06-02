from random import randrange, randint

class Node:
    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList: 
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

class Term:
    def __init__(self, coef, expo):
        self.coef = coef
        self.expo = expo

class Polynomial(LinkedList): 
    def makePoly(self, coef, expo):
        if coef != 0:
            self.append(Term(coef, expo))

    def display(self):
        node = self.head
        terms = []
        while node:
            term = node.data
            terms.append(f"{term.coef} x^{term.expo}")
            node = node.link
        print(" + ".join(terms))

    def polyAdd(self, P2):
        result = Polynomial()
        nodeA = self.head
        nodeB = P2.head

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
                coefsum = termA.coef + termB.coef
                if coefsum:
                    result.append(Term(coefsum, termA.expo))
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

if __name__ == "__main__":
    P1 = Polynomial()
    P2 = Polynomial()

    for i in range(5):
        P1.makePoly(randrange(-5, 5), randint(0, 5))
        P2.makePoly(randrange(-5, 5), randint(0, 5))

    print('Poly 1:', end=' ')
    P1.display()
    print('Poly 2:', end=' ')
    P2.display()

    P3 = P1.polyAdd(P2)
    print('Poly 3:', end=' ')
    P3.display()
