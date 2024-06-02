l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(l1 == l2)
print(l1 is l2) # 주소 같은지 묻는 것
print(l1 is not l2) # is not : 주솟값이 다른지 묻는 것

l3 = l1
print(l1 == l3)
print(l1 is l3)
print(l1 is not l3)

for i in range(5):
    print (i)

for i in range(5):
    print(i, end = ' ')
    

print()


#escape sequence
# 오류 : print(""Hello" world") 
# 오류 해결법 - escape sequence
print("\"Hello\" world")


for c in "Hello!":
    print(c, end = ' ')

print()


mySet = [12, 33, 26, 52 , 26, 99]
for e in mySet:
    print(e, end = ' ')

print()

mySet = set([12, 33, 26, 52 , 26, 99])
for e in mySet:
    print(e, end = ' ')

print()

myDict = {'A':12, 'B':33, 'C':52, 'D':26, 'E':99}

for e in myDict:
    print(e, end = ' ')

print()

#중요하댔음.
myDict = {'A':12, 'B':33, 'C':52, 'D':26, 'E':99}

for e in myDict:
    print(e, end = ' - ')
    print(myDict[e]) # key로 접근

print()

#포맷 지정자
a= 3
b=13
c=123
print(a)
print(b)
print(c)

print()

a= 3
b=13
c=123
print("%3d" %a) # : 숫자 하나당 세 자리로 출력하라.
print("%3d" %b)
print("%3d" %c)

#형식 지정자
for j in range(2, 10):
    for i in range(10):
        print("%d * %d = %2d " % (i, j, i*j) , end =  " ")


print()

s = '   Hello World   '
print(s + 'Hi')
#strip : 공백 소거
print(s.strip() + 'Hi')
#split : 문자열을 tokenizing함.
print(s.split())

s= 'Hello World,,, hi'
print(s.split())