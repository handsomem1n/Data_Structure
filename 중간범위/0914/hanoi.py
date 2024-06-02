"""
n: 옮겨야 할 원판의 수
fr: 출발 기둥의 이름(문자열)
tmp: 임시 기둥의 이름(문자열)
to: 목표 기둥의 이름(문자열)
"""
#재귀적 방법
def hanoi_tower(n, fr, tmp, to) :

    if(n == 1) :
        print("원판 1: %s --> %s" %(fr, to))
    else :
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" %(n, fr, to))
        hanoi_tower(n-1, tmp, fr, to)

hanoi_tower(3, 'a', 'b', 'c')

print('ㅡㅡㅡㅡㅡㅡㅡㅡㅡ')

# 재귀적이지 않은 방법
def hanoi_tower2(n, fr, tmp, to):
    if n == 1:
        print("%s --> %s" % (fr, to))
        return

    stack = []
    stack.append((n, fr, tmp, to))

    while stack:
        n, fr, tmp, to = stack.pop()

        if n == 1:
            print("%s --> %s" % (fr, to))
        else:
            stack.append((n - 1, tmp, fr, to))
            stack.append((1, fr, tmp, to))
            stack.append((n - 1, fr, to, tmp))

hanoi_tower2(3, 'A', 'B', 'C')

        