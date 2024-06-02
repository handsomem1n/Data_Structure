from ArrayStack import ArrayStack
from EvalPostfix import evalPostfix

# 연산자의 우선순위 계산 함수
def precedence(op):
    if op in '()': return 0
    if op in '+-': return 1
    if op in '*/': return 2
    return -1

# 중위 표기 수식의 후위식 변환
def Infix2Postfix(expr):
    s = ArrayStack(100)
    output = []

    for term in expr:
        if term == '(':
            s.push('(')
        elif term == ')':
            while not s.isEmpty():
                op = s.pop()
                if op == '(':
                    break
                else:
                    output.append(op)
        elif term in "+-*/":
            while not s.isEmpty():
                op = s.peek()
                if precedence(term) <= precedence(op):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)
        else:  # 피연산자
            output.append(term)

    while not s.isEmpty():
        output.append(s.pop())

    return output

if __name__ == "__main__":
    print('스택의 응용3: 중위표기식 후위표기 변환\n')

    # 사용자로부터 중위표기 수식을 입력받기
    infix_str = input("중위표기 수식을 입력하세요 (연산자와 피연산자는 공백으로 분리): ")
    infix_expr = infix_str.split()  # 공백을 기준으로 문자열 분리하여 리스트 생성

    postfix_expr = Infix2Postfix(infix_expr)
    result = evalPostfix(postfix_expr)

    print('  중위표기: ', ' '.join(infix_expr))
    print('  후위표기: ', ' '.join(postfix_expr))
    print('  계산결과: ', result)
