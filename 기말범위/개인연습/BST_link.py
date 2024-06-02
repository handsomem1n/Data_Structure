'''
Binary Search Tree(BST)
표현법 두 가지 : 배열 표현법과 링크 표현법 중 링크 표현법
이진 트리의 한 형태이지만 큰 차이점은 이진 트리에 비하여 특정한 정렬 순서를 지키고 있다는 점이다.
정렬 순서 : 왼쪽 자식 노드 < 루트 < 오른쪽 자식 노드 (8시 -> 12시 -> 4시 방향의 커지는 순서라고 기억해두면 좋을듯.)
연산 - 탐색 / 삽입 / 삭제
    
주의 : BST_node class는 인자를 left, right값을 받지 않는다. (9장 - 5 page 참고)


'''

class BST_Node :
    def __init__ (self, key, value) : # 
        # 이진 탐색 트리에서 각 노드는 일반적으로 두 가지 주요 정보를 가지고 있습니다: 키(key)와 값(value).
        self.key = key # 따라서, n.key : 현재 노드가 가지고 있는 key값
        self.value = value # 따라서, n.value : 현재 노드가 가지고 있는 value값
        self.left = None
        self.right = None
    

# 함수 재귀 호출로 구현
# 탐색은 항상 루트노드에서 시작
# 목표 : 현재 노드 n과 찾으려는 노드의 key값이 일치하는 경우를 찾아 그 key값을 return 한다.
def bst_search_key_recursion(n, key) : # n: 이 변수는 현재 검사하고 있는 이진 탐색 트리의 노드를 나타냅니다.() 함수가 처음 호출될 때, n은 보통 트리의 루트 노드를 가리키게 됩니다.) 
    # 이후 재귀 호출 과정에서는 트리의 왼쪽 혹은 오른쪽 서브트리의 루트 노드를 가리키게 됩니다.
    # key: key는 찾고자 하는 값의 키를 나타냅니다. 이진 탐색 트리에서 각 노드는 고유한 키 값을 가지고, 이 키를 통해 해당 노드를 식별합니다.
    if n == None :
        return None
    elif key == n.key : # 찾고자 하는 값(key) == 현재 노드의 키 값(n.key) # n.key는 이진 탐색 트리(Binary Search Tree, BST)의 노드 n에 저장된 키(key) 값을 나타냅니다.
        return n
    elif key < n.key : # 찾고자 하는 값(key) < 현재 노드의 키 값(n.key) -> 노드를 왼쪽으로 이동하고 다시 찾아보기
        return bst_search_key_recursion(n.left, key)
    elif key > n.key : # 찾고자 하는 값(key) > 현재 노드의 키 값(n.key) -> 노드를 오른쪽으로 이동하고 다시 찾아보기
        return bst_search_key_recursion(n.right , key)
    
# 탐색연산 by iterative    
def bst_search_key_iterative(n, key) :
    while n is not None :
        if key == n.key : # 찾고자하는 값 == 현재 노드의 키 값(Goal)
            return n
        elif key < n.key : # 찾고자 하는 값(key) < 현재 노드의 키 값(n.key)
            n = n.left
        elif key > n.key : # 찾고자 하는 값(key) > 현재 노드의 키 값(n.key)
            n = n.right
    return None

# 키의 최솟값
def bst_search_minimum_key(n) : # 최솟값을 찾는 데는 key 매개변수가 필요 없으므로, 매개변수는 n만 전달
    if n is None :
        return None
    while n.left is not None :
        n = n.left
    return n

# 키의 최댓값
def bst_search_maximun_key(n, key) : 
    if n is None :
        return None
    while n.right is not None :
        n = n.right
    return n

# 값을 이용한 탐색
def bst_search_value (n, value):
    if n is None :
        return None
    elif value == n.value : # 내가 찾으려는 value  == 현재 탐색중인 노드의 value -> 현재 탐색중인 노드를 return (Goal)
        return n
    


    # 왼쪽 서브트리에서 탐색 - 왼쪽 서브트리에서 못 찾을 경우 오른쪽으로 갈 거임.
    residue = bst_search_value(n.left, value) # residue = bst_search_value(n.left, value)를 호출하여 왼쪽 서브트리에서 value 값을 가진 노드를 찾습니다.
    # 각 재귀 호출에서는 새로운 서브트리의 루트 노드가 n이 됩니다. 함수는 일치하는 value를 찾거나, 더 이상 탐색할 노드가 없을 때까지 계속 재귀 호출을 수행합니다.

    if residue is not None : # 왼쪽 서브트리에서 탐색 - 왼쪽 서브트리에서 못 찾을 경우 오른쪽으로 갈 거임.
        return residue
    
    else : # 왼쪽 서브트리에서 못 찾았으니 오른쪽 서브트리에서 찾자
        return bst_search_value(n.right, value)
    

def bst_insert(n, insert_node) : # # n: 이 변수는 현재 검사하고 있는 이진 탐색 트리의 노드를 나타냅니다.() 함수가 처음 호출될 때, n은 보통 트리의 루트 노드를 가리키게 됩니다.) / node : 삽입할 노드
    if n == None :
        return insert_node # (Goal)
    if insert_node.key == n.key : # 넣으려는 노드의 키 값 == 현재 검사하고 있는 노드의 키 값 -> 중복이라는 거임
        return n # 현재 검사하고 있는 노드 반환
    
    if n.key > insert_node.key : # 현재 검사중인 노드의 키 > 넣으려는 노드의 키 -> 
        n.left = bst_insert(n.left, insert_node)
    elif n.key < insert_node.key : # 현재 검사중인 노드의 키 < 넣으려는 노드의 키 -> 
        n.right = bst_insert(n.right, insert_node)

    return n

def bst_delete(n, key) :
    '''
    1. 말단 노드를 삭제할 때
    2. 자식이 하나일 때
    3. 자식이 둘 일 때
    '''
    
    if n == None :
        return n
    
    if n.key < key : # 삭제할 노드 < 현재 검사중인 노드(루트 노드) -> 왼쪽
        n.left = bst_delete(n.left , key)
    elif n.key > key : # 삭제할 노드 > 현재 검사중인 노드(루트 노드) -> 오른쪽
        n.right = bst_delete(n.right, key)
    else : # 위의 두 조건을 둘 다 만족하지 않는다 -> 현재 검사중인 노드 n을 삭제한다.
        # case1 아니면, case2 중 오른쪽 자식만 있는 경우
        if n.left == None : # 왼쪽이 비었다 ->
            return n.right # 오른쪽 삭제
        # case2 중 왼쪽 자식만 있는 경우
        if n.right == None :
            return n.left
        
        # case3 
        # 3-1. 후계자 고르기
        successor_minimun = bst_search_minimum_key(n.right) # 매개변수로는 n.right이다. 제일 큰 애들 중 최솟값을 골라야 하니.
        successor_maximum = bst_search_maximun_key(n.left) # 매개변수로는 n.left이다. 제일 작은 애들 중 최댓값을 골라야 하니.
        # 3-2. 후계자의 값을 삭제할 노드의 값으로 붙여넣음
        n.key = successor_maximum.key #(minimum값으로 선택하였음)
        #value도 해줌.
        n.value = successor_maximum.value 
        # 3-3. 후계자 삭제
        n.right = bst_delete(n.right, successor_maximum.key)
    return n
        



