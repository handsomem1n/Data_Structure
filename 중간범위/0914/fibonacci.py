def rFib(n):
    if n ==0 :
        return 0
    elif n == 1:
        return 1
    else :
        return rFib(n-2) + rFib(n-1)
    

print ('rFib : %d' %(rFib(10)))

def iFib(n) :
    if ( n < 2) :
        return n
    pp = 0
    p = 1

    for i in range (2,n+1):
        current = p + pp
        pp = p
        p = current

    return current
print ('iFib : %d' %iFib(10))