
# 코드 7.11: 해시 테이블 및 해시 함수 준비
M = 13                  # 해시 테이블의 크기
table = [None]*M        # 해시 테이블. 모든 항목은 None으로 초기화

def hashFn(key) :     # 해시 함수로는 제산함수 사용
    return key % M

# 코드 7.12: 선형조사법의 삽입 연산
def insert(key) :
    i = hashFn(key)
    count = M
    while count > 0 :
        if table[i] == None or table[i] == -1: # 찾은 경우
            break # while문 나가라
        # 못 찾은 경우
        i = (i+1) % M #시계방향 다음 index
        count -=1 # 무한정 돌순없으니
    # 찾은 경우에서 i 인덱스를 들고 나왔으니
    # if count >  0 :
    table[i] = key # 삽입 완료

    
# 코드 7.13: 선형조사법의 탐색 연산
def search(key) :
    i = hashFn(key)
    count = M
    while count > 0:
        if table[i] == key :
            # return i
            return table[i]
        if table[i] == None :
            return None
        i = (i+1) % M
        count -=1
        

# 코드 7.14: 선형조사법의 삭제 연산
def delete(key) :
    i = hashFn(key)
    count = M
    while count > 0 :
        #삭제할 인덱스를 찾아야겠지
        if table[i] == key :
            table[i] = -1 # None이 아니다
            return
        if table[i] == None : #못찾은 경우
            return 
        i = (i+1) % M
        count -=1

#======================================================================
# 코드 7.15: 선형조사법의 테스트 프로그램
if __name__ == "__main__":
    data = [45, 27, 88, 9, 71, 60, 46, 38, 24]
    for d in data :
        print( "h(%2d)=%2d" %(d,hashFn(d)), end=' ')
        insert(d)
        print(table)

    print("46탐색-->", search(46))
    print("39탐색-->", search(39))

    print("60삭제-->", end='')
    delete(60)
    print(table)
    print("46삭제-->", end='')
    delete(46)
    print(table)


