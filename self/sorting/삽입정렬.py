'''
정렬 안된 상태의 영역 / 정렬 된 상태의 영역
정렬 안된 영역에서, 적절한 값을 정렬 된 영역에 끼워넣음.
'''
def insertion_sort(list) :
    n = len(list)
    for i in range(1, n) :
        key = list[i]
        j = i-1
        while j>=0 and key < list[j] :
            list[j+1] = list[j]
            j =j-1 
        list[j+1] = key
        print(list, i )




a = [5,3,8,4,9,1,6,2,7]
print(a)
print('--시작--')
insertion_sort(a)
print('--결과--')
print(a)