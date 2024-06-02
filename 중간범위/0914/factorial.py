#반복법
def factorial_iter(n) : 
    result = 1
    for k in range(1, n+1) : 
        result = result * k
    return result
print(factorial_iter(4))

#순환법
def factorial(n) : 
    if n == 1 :
        return 1
    else :
        return n * factorial(n-1)
print(factorial(6))