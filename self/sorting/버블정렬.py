'''
(첫번째부터 끝까지)
    양 옆 인접한 숫자를 비교하여 정렬 -> 양
'''

def bubblesort(list) :
    n = len(list)
    for i in range(n) :
        changed = False
        for j in range(0, n-i-1) :
            if list[j] > list[j+1] :
                list[j], list[j+1] = list[j+1], list[j]
                changed = True
        if changed == False : break

        # while j<= n-1 and list[j] > list[j+1] :
        #     list[j], list[j+1] = list[j+1], list[j]
        #     j= j+1
        print(list, i+1)
    
    

a = [5,3,8,4,9,1,6,2,7] 
# a = [1,2,3,4,5,6,7,8,9] # best 케이스
# a = [9,8,7,6,5,4,3,2,1] # worst 케이스
print(a)
print('--시작--')
bubblesort(a)
print('--결과--')
print(a)