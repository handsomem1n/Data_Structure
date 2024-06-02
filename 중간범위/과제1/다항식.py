class Polynomial:
    def __init__(self, coefficients=[]): # 계수들을 차수가 높은 것에서 낮은 것으로 저장
        self.coefficients = coefficients

    def degree(self): # 다항식의 차수는 리스트 길이에서 1을 뺀 값
        return len(self.coefficients) - 1

    def evaluate(self, scalar): # 차수가 높은 것부터 시작하여 낮은 것으로 계산
        result = 0
        for i in range(self.degree(), -1, -1):
            result = result * scalar + self.coefficients[i]
        return result

    def add(self, other): # 두 다항식 중 더 차수가 큰 다항식의 차수를 기준으로 합산
        max_degree = max(self.degree(), other.degree())
        result_coefficients = [0] * (max_degree + 1)

        for i in range(max_degree + 1):
            if i <= self.degree():
                result_coefficients[i] += self.coefficients[i]
            if i <= other.degree():
                result_coefficients[i] += other.coefficients[i]

        return Polynomial(result_coefficients)

    def display(self):  # 입력받은 정수배열로 다항식을 문자열 형태로 변환
        for i in range(self.degree(), -1, -1):
            coef = self.coefficients[i]
            if i == 0:
                print(coef, end='')
            else:
                print("%dx^%d" % (coef, i), end='')
            if i != 0:
                print(" + ", end='')
        print()


    def cin(self): # read(). 계수들을 차례대로 입력받음 / 거꾸로 재배열
        input_values = list(map(int, input("input degrees in order : ").split())) #
        self.coefficients = []

        for i in range(len(input_values) - 1, -1, -1): # 리스트의 마지막 요소부터 첫 요소까지 반복, 입력된 계수들을 차수가 높은 것에서 낮은 것으로 저장
            self.coefficients.append(input_values[i])

if __name__ == '__main__':
    a = Polynomial()
    b = Polynomial()

    a.cin()
    b.cin()
    print('A(x) = ', end = ' ')
    a.display()
    print('B(x) = ', end = ' ')
    b.display()

    c = a.add(b)
    print('C(x) = ', end = ' ')
    c.display()
    
    n = 2
    print('C(%d) = ' % n, end=' ')
    print(c.evaluate(n))