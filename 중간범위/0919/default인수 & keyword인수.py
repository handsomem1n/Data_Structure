# default인수
def sum_range(begin, end, step= 1) : # step쪽은 안써도됨(default step = 1)
    sum = 0
    for i in range(begin, end, step):
        sum += i

    return sum

print ('sum =', sum_range(1, 10))
print('sum =', sum_range(1, 10, 2))

# keyword인수
print('sum =', sum_range(step =3,begin=1, end=10))
