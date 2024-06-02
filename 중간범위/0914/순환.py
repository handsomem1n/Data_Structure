def recursiveFact(n):
    if n == 1 : 
        return 1
    else : 
        return n * recursiveFact(n-1)
    
# 함수 호출
result = recursiveFact(5)

# 함수 호출 결과를 출력
print('recursiveFact : %d' % result)