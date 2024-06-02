# 정렬된 배열에서 사용
def binary_search(list, e, low, high) :
    mid = (low + high) // 2
    
    if list[mid] == e :
        return mid
    elif list[mid] < e :
        low = mid
        return binary_search(list, low+1, high)
    elif list[mid] > e :
        high = mid
        return binary_search(list, low, high-1)
    

if __name__ == 'main' :
    a = [1,2,3,4,5,6,7,8,9,10,11]
    low = 0
    high = len(a)-1
    
    print(binary_search(a, 9, low, high))