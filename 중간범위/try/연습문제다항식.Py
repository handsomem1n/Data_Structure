class Term:
    def __init__(self, coef, expo):
        self.coef = coef  # 계수
        self.expo = expo  # 지수

class SparsePoly(LinkedList):
    def __init__(self):
        super().__init__()

    def read(self, terms):
        '''항들을 읽어서 연결리스트에 저장'''
        for coef, expo in terms:
            if coef != 0:
                self.append(Term(coef, expo))

    def display(self):
        '''다항식을 출력'''
        node = self.head
        terms = []
        while node:
            term = node.data
            terms.append(f"{term.coef}x^{term.expo}")
            node = node.link
        return " + ".join(terms)

    def add(self, polyB):
        '''다항식 덧셈을 수행'''
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
            else:  # termA.expo == termB.expo
                new_coef = termA.coef + termB.coef
                if new_coef:
                    result.append(Term(new_coef, termA.expo))
                nodeA = nodeA.link
                nodeB = nodeB.link

        # 한쪽 리스트의 노드들이 남아있을 경우 추가
        while nodeA is not None:
            termA = nodeA.data
            result.append(Term(termA.coef, termA.expo))
            nodeA = nodeA.link

        while nodeB is not None:
            termB = nodeB.data
            result.append(Term(termB.coef, termB.expo))
            nodeB = nodeB.link

        return result

# 예제:
polyA = SparsePoly()
polyA.read([(3, 12), (2, 8), (1, 0)])
print(polyA.display())  # 3x^12 + 2x^8 + 1x^0

polyB = SparsePoly()
polyB.read([(8, 12), (1, 10), (-1, 8), (2, 3)])
print(polyB.display())  # 8x^12 + 1x^10 - 1x^8 + 2x^3

polyC = polyA.add(polyB)
print(polyC.display())  # 11x^12 + 1x^10 + 1x^8 + 2x^3 + 1x^0
