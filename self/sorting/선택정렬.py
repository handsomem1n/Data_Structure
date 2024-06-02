'''
정렬 된 상태의 영역 / 정렬 안된 상태의 영역
list를 받아서
정렬이 안된 영역에서 최솟값을 골라, 교환해줌(0번부터 n-1까지)
'''

def selection_sort(list) :
    n = len(list)
    for i in range(n-1) :
        
        '''
        minindex=0 아님
        '''
        minindex=i
        '''
        j = i+1
        for j in range(n) :
        '''
        for j in range(i+1, n ) :
            if list[minindex] > list[j] :
                # swap(list[i], list[j])
                minindex = j
        
        list[i], list[minindex] = list[minindex], list[i]
        print(list, i+1)




a = [5,3,8,4,9,1,6,2,7]
print(a)
print('--시작--')
selection_sort(a)
print('--결과--')
print(a)
