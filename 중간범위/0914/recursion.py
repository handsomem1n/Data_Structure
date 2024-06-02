# 반복문과 순환문
def iPower(x, n):
    result = 1
    for i in range(n):
        result *= x

    return result


def rPower(x, n):
    if n == 0:
        return 1
    elif (n%2) == 0:
        return rPower(x*x, n//2)
    else :
        return x * rPower(x*x, (n-1)//2)

print ('iPower : %d' %(iPower(2, 10)))
print ('rPower : %d' %(rPower(2, 10)))

# n이 10억일때, ipower는 10억번, rPower는 30번(?)만에 실행