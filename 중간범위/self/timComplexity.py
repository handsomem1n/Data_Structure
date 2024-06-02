def a(i) :
    if i > 1:
        a(i/2)
        a(i/2)
    print("*", end=' ')
a(5)

def a(n) :
    sum = 0
    for i in range(n) :
        for j in range(i+1, n+1) :
            sum = sum + j
    return sum 
print(a(5))

def a(n) :
    i = n
    sum = 0
    if i % 3 ==0 :
        for j in range( n / 2) :
            sum +=j
    elif i % 2 == 0 :
        for j in range(5) :
            sum += j
    else :
        for j in range(n):
            sum +=j
    return sum
    #Best Case 복잡도: O(1)
    #worst case : O(n)

def whattime(second) :
    h = second / 3600
    second %= 3600
    m = second / 60
    # s = m % 60
    s = second % 60
    # return h, m, s
    print('%d 시간 %d분 %d초' %(h, m, s))

whattime(5121)
