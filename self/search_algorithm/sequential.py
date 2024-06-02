def sequential_search(list, e) :
    n = len(list)
    index =0
    for i in range(n) :
        if list[i] == e :
            index = i
    if index == 0 :
        print('없음')
        return
    return index


a = [1,2,3,4,5,6,7,8]
print(sequential_search(a, 9))